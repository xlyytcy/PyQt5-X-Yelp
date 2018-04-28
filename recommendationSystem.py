
# coding: utf-8

# # This is the main Jupyter Notebook file for this project

# In[1]:


# import seaborn #Seaborn is a Python visualization library based on matplotlib. It provides a high-level
               #interface for drawing attractive statistical graphics.


# In[2]:


# import vaderSentiment #“VADER: A Parsimonious Rule-based Model for Sentiment Analysis of Social Media Text.”
                      #published at ICWSM-14


# In[3]:


import pandas as pd
import numpy as np
import scipy
import matplotlib.pyplot as plt


# ### Load in CSV file
# - Since pandans use data format of CSV, MySQl is not used here.
# - JSON file will be host on Google Drive using the Drive API (Option 1)
# - Load local JSON (Option 2)

# In[4]:


# Read from Google Drive API
# client_id = '246749435321-4kau6brtf8m7sn3rrsqnln6jrtm892ge.apps.googleusercontent.com' # open('hello.txt', 'w').read()
# client_secret = 'ZVUispy3UNtwG5PxTOhWvRN3' # open('hello.txt', 'w').read()
#
# import oauth2client.client, oauth2client.file, oauth2client.tools
# import gspread
# flow = oauth2client.client.OAuth2WebServerFlow(client_id, client_secret, 'https://spreadsheets.google.com/feeds')
# storage = oauth2client.file.Storage('credentials.dat')
# credentials = storage.get()
# if credentials is None or credentials.invalid:
#     import argparse
#     flags = argparse.ArgumentParser(parents=[oauth2client.tools.argparser]).parse_args([])
#     credentials = oauth2client.tools.run_flow(flow, storage, flags)
#
# gc = gspread.authorize(credentials)


# Load in CSV Files

# In[5]:


csv_reviews = pd.read_csv('/Users/XG/Documents/Yelp_DB/yelp-dataset/yelp_review.csv')
csv_business = pd.read_csv('/Users/XG/Documents/Yelp_DB/yelp-dataset/yelp_business.csv')
csv_user = pd.read_csv('/Users/XG/Documents/Yelp_DB/yelp-dataset/yelp_user.csv')


# In[6]:


#csv_reviews.shape


# In[7]:


#csv_reviews.head()


# In[8]:


#csv_user.head()


# In[9]:


#csv_business.head()


# In[10]:


#csv_business.describe()


# In[11]:


csv_reviews.describe()


# ### Recommendation System

# In[12]:


user = csv_user[csv_user.review_count > 15]
business = csv_business[csv_business.review_count > 20]


# In[13]:


business.groupby('state').size()


# In[14]:


business = business.groupby('state').filter(lambda r: len(r) > 20)


# In[15]:


#business.describe()


# In[16]:


business.groupby('state').size()


# In[17]:


merged_df = pd.merge(pd.merge(csv_reviews, business, on = 'business_id'), user, on = 'user_id')


# In[18]:


#merged_df.shape


# In[19]:


#merged_df.head()


# In[20]:


merged_df.drop(merged_df.columns.difference(['business_id', 'user_id', 'stars_x']), axis = 1, inplace = True)


# In[21]:


merged_df.shape


# In[22]:


merged_df.head()


# In[23]:


for _ in range(5):
    merged_df = merged_df.groupby('business_id').filter(lambda r: len(r) >= 20)
    merged_df = merged_df.groupby('user_id').filter(lambda r: len(r) >= 15)
merged_df.shape


# In[24]:


merged_df.groupby('user_id').size()


# In[25]:


merged_df.stars_x = merged_df.stars_x.astype(int)


# In[26]:


merged_df.groupby('user_id').size()


# In[27]:


Y = pd.pivot_table(merged_df, index = 'business_id', columns = 'user_id', values = 'stars_x')


# In[28]:


Y.shape


# In[29]:


Y.describe


# In[30]:


Y.head


# In[31]:


for _ in range(10):
    Y = Y.dropna(thresh=15, axis=0)
    Y = Y.dropna(thresh=20, axis=1)


# In[32]:


Y.shape


# In[33]:


Y.count(axis=0).min()


# In[34]:


Y.count(axis=1).min()


# In[37]:


test_split_ratio = 0.3
test_size = int(Y.shape[1] * test_split_ratio)
train_size = Y.shape[1] - test_size
rand_column_mask = np.random.choice(Y.shape[1], test_size, replace = False)


# In[38]:


Y_test = Y.iloc[:, rand_column_mask].copy()


# In[39]:


for col in Y_test:
    mask_size = 5
    mask = np.random.choice(Y_test[col].notnull().nonzero()[0], mask_size, replace = False)
    Y_test[col][mask] = np.nan


# In[40]:


Y_test.count().sum()


# In[41]:


value_locations_premask = Y.iloc[:,rand_column_mask][Y.iloc[:,rand_column_mask].notnull()].stack().index.tolist()


# In[42]:


value_locations_masked = Y_test[Y_test.notnull()].stack().index.tolist()
test_values_locations = list(set(value_locations_premask) - set(value_locations_masked))
test_values_locations = pd.DataFrame.from_records(test_values_locations, columns=['business_id', 'user_id'])
query_rows = test_values_locations.business_id
rows = Y.index.values
sidx = np.argsort(rows)
row_ids = sidx[np.searchsorted(rows,query_rows,sorter=sidx)]
query_cols = test_values_locations.user_id
cols = Y.columns.values
sidx = np.argsort(cols)
col_ids = sidx[np.searchsorted(cols,query_cols,sorter=sidx)]
Y_test_original = Y.iloc[:,rand_column_mask].copy()
Y.iloc[:,rand_column_mask] = Y_test.copy()
Y.count().sum()


# In[45]:


R = Y.notnull()


# In[43]:


def cost(params, Y, R, num_business, num_user, num_features, lamda):
    # lamda is the regularization coefficient lambda (python keyword)
    # Convert the dataframe to ndarray, fill nans with zeros, and leave the answer array for easier linear algebra operations
#     Y_mat = np.nan_to_num(Y.as_matrix())
#     R_mat = np.nan_to_num(R.as_matrix())

    # unfold X and theta from the 1D params array
    X = np.reshape(params[:num_business*num_features], (num_business, num_features))
    theta = np.reshape(params[num_business*num_features:], (num_user, num_features))    
    
    J = 0.5*np.sum(pow((X@theta.T - Y)*R,2)) + lamda/2*(np.sum(pow(theta,2)) + np.sum(pow(X,2)))
    
    X_grad = (X@theta.T - Y)*R@theta + lamda*X
    theta_grad = (X@theta.T - Y).T * R.T@X + lamda*theta
    
    grad = np.concatenate((np.ravel(X_grad), np.ravel(theta_grad)))
    print('The cost is currently equal to.........', J)
    return J, grad


# In[46]:


num_features = 75
num_business = Y.shape[0]
num_user = Y.shape[1]

lamda = 10

X = np.random.randn(num_business, num_features)
theta = np.random.randn(num_user, num_features)
params = np.concatenate((np.ravel(X), np.ravel(theta)))

Y_mat = Y.as_matrix()

Ymean = np.nanmean(Y_mat, axis=1, keepdims=True)

Y_mat = np.nan_to_num(Y_mat)
R_mat = np.nan_to_num(R.as_matrix())

# Ymean = np.zeros((num_business, 1))  
# Ynorm = np.zeros((num_business, num_user))

Ynorm = np.nan_to_num(Y.subtract(Y.mean(axis=1), axis=0).as_matrix())


# In[49]:


from scipy.optimize import minimize

fmin = minimize(fun=cost, x0=params, args=(Ynorm, R_mat, num_business, num_user, num_features, lamda),  
                method='CG', jac=True, options={'maxiter': 100})
X = np.matrix(np.reshape(fmin.x[:num_business * num_features], (num_business, num_features)))  
theta = np.matrix(np.reshape(fmin.x[num_business * num_features:], (num_user, num_features)))


# In[50]:


predictions = X * theta.T + Ymean


# In[51]:


predictions[0,162]


# In[52]:


((np.round(predictions[row_ids, col_ids]) >= 3) & (Y_test_original.lookup(test_values_locations.business_id, test_values_locations.user_id) >= 3) | 
 (predictions[row_ids, col_ids] < 3) & (Y_test_original.lookup(test_values_locations.business_id, test_values_locations.user_id) < 3)).mean()


# In[53]:


all_value_idx = Y[Y.notnull()].stack().index.tolist()
all_value_idx


# In[54]:


def recommend(Y, predictions, user_id):
    # get index position of user_id
    user_idx = Y.columns.get_loc(user_id)    
    # find index positions of non reviewed businesses for this user:
    all_recommendation_indices = np.squeeze(np.asarray(np.argsort(predictions[:,user_idx], axis=0)[::-1]))
    # find reviewed businesses, find predictions(recommendations) for our user, return businesses in descending sorted order
    # remove reviewed businesses from recommendations
    rated_businesses = [Y.loc[:,user_id].index.get_loc(i) for i in Y.loc[:,user_id][Y.loc[:,user_id].notnull()].index.tolist()]
    all_recommendation_indices = all_recommendation_indices[~np.in1d(all_recommendation_indices,rated_businesses)]
    return Y.index[all_recommendation_indices], all_recommendation_indices


# In[55]:


recommended_business_names, recommended_business_idx = recommend(Y, predictions, Y.columns[1])


# In[57]:


business.set_index('business_id', drop=False, verify_integrity=True, inplace=True)

business.loc[recommended_business_names][:3]


# In[59]:


recommended_business_names, recommended_business_idx = recommend(Y, predictions, Y.columns[90])
business.set_index('business_id', drop=False, verify_integrity=True, inplace=True)
business.loc[recommended_business_names][:3]

