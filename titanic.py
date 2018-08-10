import pandas as pd


titanic_df = pd.read_csv('dataset/train.csv')
test_df = pd.read_csv('dataset/test.csv')


print titanic_df.head()
titanic_df.info()