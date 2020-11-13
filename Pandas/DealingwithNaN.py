import pandas as pd

# We create a list of Python dictionaries
items2 = [{'bikes': 20, 'pants': 30, 'watches': 35, 'shirts': 15, 'shoes':8, 'suits':45},
{'watches': 10, 'glasses': 50, 'bikes': 15, 'pants':5, 'shirts': 2, 'shoes':5, 'suits':7},
{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4, 'shoes':10}]

# We create a DataFrame  and provide the row index
store_items = pd.DataFrame(items2, index = ['store 1', 'store 2', 'store 3'])

print(store_items)

# We count the number of NaN values in store_items

x = store_items.isnull().sum().sum()
# We print x
print('Number of NaN values in our DataFrame:', x)
x = store_items.notnull().sum().sum()
print('Number of notNaN values in our DataFrame:', x)

# remove NaN values
y = store_items.dropna(axis=0)
print(y)
z = store_items.dropna(axis=1)
print(z)

# replace NANs
c = store_items.fillna(0)
print(c)

# We replace NaN values with the previous value in the column
d = store_items.fillna(method = 'ffill', axis = 0)
print(d)
# We replace NaN values with the previous value in the row
f = store_items.fillna(method = 'ffill', axis = 1)
print(f)
# We replace NaN values with the next value in the column
g = store_items.fillna(method = 'backfill', axis = 0)
print(g)
# We replace NaN values with the next value in the row
h = store_items.fillna(method = 'backfill', axis = 1)
print(h)
# We replace NaN values by using linear interpolation using column values
j = store_items.interpolate(method = 'linear', axis = 0)
print(j)
# We replace NaN values by using linear interpolation using row values
k = store_items.interpolate(method = 'linear', axis = 1)
print(k)