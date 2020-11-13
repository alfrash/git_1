import pandas as pd

# A list of pyton dicts
items = [
    {'x': 20, 'y': 30, 'z': 140},
    {'x': 20, 'y': 30, 'z': 140, 'p': 3.14}
]
e = pd.DataFrame(items, index=['Axis1', 'Axis2'])
print('e =',e)

# access columns Label
print(e[['x']])
print(e[['x', 'y']])

# access row
print(e.loc[['Axis2']])

# access column and row
print(e['x']['Axis1'])

# Add column
e['v'] = [15,2]
print(e)
e['sum'] = e['x'] + e['y']
print(e)

stors = [
    {'bikes': 20, 'pants': 30, 'watches': 35},
    {'watches': 40, 'glasses': 10, 'pants': 50, 'bikes': 15}
]

x = pd.DataFrame(stors, index=['store1', 'store2'])

# add row
newItems = [{'bikes': 20, 'pants': 30, 'watches': 35, 'glasses': 4}]
newStore = pd.DataFrame(newItems, index=['store3'])

x = x.append(newStore)
print(x)

# add column
x['newWatches'] = x['watches'][1:]

x.insert(4,'shose',[8,5,0])
print(x)

# deleting
x.pop('newWatches')
x = x.drop('pants',axis=1)
x = x.drop(['store1', 'store2'], axis=0)
print(x)

# rename
x = x.rename(columns={'bikes': 'hats'})
x = x.rename(index={'store3': 'last store'})
x = x.set_index('hats')

print(x)
