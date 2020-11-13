import pandas as pd

groceries = pd.Series(data=[30,6,'yes','no'],index=['eggs', 'apples', 'milk', 'bread'])
print(groceries)
print(groceries.shape)
print(groceries.ndim)
print(groceries.size)
print(groceries.values)
print(groceries.index)
print('banana' in groceries)


# lesson 5 - Accessing and Deleting Elements in Pandas Series

print(groceries['eggs'])
print(groceries[['milk','bread']])
print(groceries[0])
print(groceries[-1])
print(groceries[[0,1]])
print(groceries.loc[['eggs','apples']])
print(groceries.iloc[[2,3]])

# modify
groceries['eggd'] = 2
print(groceries)

# deleting
x = groceries.drop('apples') # create a new list dose not delete from the origenal
print('x =',x)

# deleting in place
groceries.drop('apples', inplace=True)
print(groceries)