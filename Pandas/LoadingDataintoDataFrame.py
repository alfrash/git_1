import pandas as pd

# We load Google stock data in a DataFrame
Google_stock = pd.read_csv('/Users/ahmedalfrash/Desktop/AI-project/Pandas/GooG.csv')

# We print some information about Google_stock
# print('Google_stock is of type:', type(Google_stock))
# print('Google_stock has shape:', Google_stock.shape)
print(Google_stock)
# print(Google_stock.head())
# print(Google_stock.tail())
# print(Google_stock.head(2))
# print(Google_stock.tail(5))

print(Google_stock.isnull().any())
# We get descriptive statistics on our stock data
print(Google_stock.describe())
# We get descriptive statistics on a single column of our DataFrame
Google_stock['Adj Close'].describe()
# We print information about our DataFrame  
print()
print('Maximum values of each column:\n', Google_stock.max())
print()
print('Minimum Close value:', Google_stock['Close'].min())
print()
print('Average value of each column:\n', Google_stock.mean())
# We display the correlation between columns
print()
print(Google_stock.corr())

x = Google_stock.groupby(['Date'])['Open'].sum()
print('x =',x)
x = Google_stock.groupby(['Date'])['Open'].mean()
print('x =',x)


