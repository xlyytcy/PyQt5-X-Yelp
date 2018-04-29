import pandas as pd

csv_reviews = pd.read_csv('/Users/XG/Documents/Yelp_DB/yelp-dataset/yelp_review.csv')
csv_business = pd.read_csv('/Users/XG/Documents/Yelp_DB/yelp-dataset/yelp_business.csv')
csv_user = pd.read_csv('/Users/XG/Documents/Yelp_DB/yelp-dataset/yelp_user.csv')

user = csv_user[csv_user.review_count > 15]
business = csv_business[csv_business.review_count > 20]
business = business.groupby('state').filter(lambda r: len(r) > 20)
business.set_index('business_id', drop=False, verify_integrity=True, inplace=True)
