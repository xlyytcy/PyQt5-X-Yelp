import pickle
import os.path
import numpy as np
import pandas as pd


csv_business = pd.read_csv('/Users/XG/Documents/Yelp_DB/yelp-dataset/yelp_business.csv')
csv_user = pd.read_csv('/Users/XG/Documents/Yelp_DB/yelp-dataset/yelp_user.csv')

user = csv_user[csv_user.review_count > 15]
business = csv_business[csv_business.review_count > 20]
business = business.groupby('state').filter(lambda r: len(r) > 20)
business.set_index('business_id', drop=False, verify_integrity=True, inplace=True)

file_path1 = '/Users/XG/.venv/YelpxPython/Y_df.pkl'
n_bytes = 2 ** 31
max_bytes = 2 ** 31 - 1
data = bytearray(n_bytes)

bytes_in = bytes_in2 = bytearray(0)
input_size = os.path.getsize(file_path1)
with open(file_path1, 'rb') as f_in:
    for _ in range(0, input_size, max_bytes):
        bytes_in += f_in.read(max_bytes)
Y = pickle.loads(bytes_in)

predictions = np.asmatrix(np.load('/Users/XG/.venv/YelpxPython/predic.npy'))


def recommend(user_id):
    # get index position of user_id
    user_idx = Y.columns.get_loc(user_id)
    # find index positions of non reviewed businesses for this user:
    all_recommendation_indices = np.squeeze(np.asarray(np.argsort(predictions[:,user_idx], axis=0)[::-1]))
    # find reviewed businesses, find predictions(recommendations) for our user, return businesses in descending sorted order
    # remove reviewed businesses from recommendations
    rated_businesses = [Y.loc[:,user_id].index.get_loc(i) for i in Y.loc[:,user_id][Y.loc[:,user_id].notnull()].index.tolist()]
    all_recommendation_indices = all_recommendation_indices[~np.in1d(all_recommendation_indices,rated_businesses)]
    return Y.index[all_recommendation_indices], all_recommendation_indices


# recommended_business_names, recommended_business_idx = recommend(Y.columns[90])
# print(business.loc[recommended_business_names][:3])
