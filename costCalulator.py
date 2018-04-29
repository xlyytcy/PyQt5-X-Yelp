from fileParser import business, csv_reviews, user
import pandas as pd
import numpy as np
from scipy.optimize import minimize

merged_df = pd.merge(pd.merge(csv_reviews, business, on='business_id'), user, on='user_id')

merged_df.drop(merged_df.columns.difference(['business_id', 'user_id', 'stars_x']), axis=1, inplace=True)

for _ in range(5):
    merged_df = merged_df.groupby('business_id').filter(lambda r: len(r) >= 20)
    merged_df = merged_df.groupby('user_id').filter(lambda r: len(r) >= 15)

merged_df.stars_x = merged_df.stars_x.astype(int)

Y = pd.pivot_table(merged_df, index='business_id', columns='user_id', values='stars_x')

for _ in range(10):
    Y = Y.dropna(thresh=15, axis=0)
    Y = Y.dropna(thresh=20, axis=1)

test_split_ratio = 0.3
test_size = int(Y.shape[1] * test_split_ratio)
train_size = Y.shape[1] - test_size
rand_column_mask = np.random.choice(Y.shape[1], test_size, replace=False)

Y_test = Y.iloc[:, rand_column_mask].copy()

for col in Y_test:
    mask_size = 5
    mask = np.random.choice(Y_test[col].notnull().nonzero()[0], mask_size, replace=False)
    Y_test[col][mask] = np.nan

value_locations_premask = Y.iloc[:, rand_column_mask][Y.iloc[:, rand_column_mask].notnull()].stack().index.tolist()

value_locations_masked = Y_test[Y_test.notnull()].stack().index.tolist()
test_values_locations = list(set(value_locations_premask) - set(value_locations_masked))
test_values_locations = pd.DataFrame.from_records(test_values_locations, columns=['business_id', 'user_id'])
query_rows = test_values_locations.business_id
rows = Y.index.values
sidx = np.argsort(rows)
row_ids = sidx[np.searchsorted(rows, query_rows, sorter=sidx)]
query_cols = test_values_locations.user_id
cols = Y.columns.values
sidx = np.argsort(cols)
col_ids = sidx[np.searchsorted(cols, query_cols, sorter=sidx)]
Y_test_original = Y.iloc[:, rand_column_mask].copy()
Y.iloc[:, rand_column_mask] = Y_test.copy()
Y.count().sum()

R = Y.notnull()


def cost(params, Y, R, num_business, num_user, num_features, lamda):
    X = np.reshape(params[:num_business * num_features], (num_business, num_features))
    theta = np.reshape(params[num_business * num_features:], (num_user, num_features))

    J = 0.5 * np.sum(pow((X @ theta.T - Y) * R, 2)) + lamda / 2 * (np.sum(pow(theta, 2)) + np.sum(pow(X, 2)))

    X_grad = (X @ theta.T - Y) * R @ theta + lamda * X
    theta_grad = (X @ theta.T - Y).T * R.T @ X + lamda * theta

    grad = np.concatenate((np.ravel(X_grad), np.ravel(theta_grad)))
    print('The cost is currently equal to.........', J)
    return J, grad


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

Ynorm = np.nan_to_num(Y.subtract(Y.mean(axis=1), axis=0).as_matrix())

fmin = minimize(fun=cost, x0=params, args=(Ynorm, R_mat, num_business, num_user, num_features, lamda),
                method='CG', jac=True, options={'maxiter': 100})
X = np.matrix(np.reshape(fmin.x[:num_business * num_features], (num_business, num_features)))
theta = np.matrix(np.reshape(fmin.x[num_business * num_features:], (num_user, num_features)))

predictions = X * theta.T + Ymean

((np.round(predictions[row_ids, col_ids]) >= 3) & (
        Y_test_original.lookup(test_values_locations.business_id, test_values_locations.user_id) >= 3) |
 (predictions[row_ids, col_ids] < 3) & (
         Y_test_original.lookup(test_values_locations.business_id, test_values_locations.user_id) < 3)).mean()

all_value_idx = Y[Y.notnull()].stack().index.tolist()

