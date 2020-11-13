import pandas as pd

items = {
    'Bob': pd.Series(data = [245, 25, 55], index = ['bike', 'pants', 'watch']),
    'Alice': pd.Series(data = [40, 110, 550, 45], index = ['book', 'glasses', 'pants', 'bike'])
}

shoping_Carts = pd.DataFrame(items)
print(shoping_Carts)

data = {
    'Bob': pd.Series(data = [245, 25, 55]),
    'Alice': pd.Series(data = [40, 110, 550, 45])
}

x = pd.DataFrame(data)
print(x)

print(shoping_Carts.index)
print(shoping_Carts.columns)
print(shoping_Carts.values)

print(shoping_Carts.shape)
print(shoping_Carts.ndim)
print(shoping_Carts.size)

a = pd.DataFrame(items,columns=['Bob'])
print('a =',a)
b = pd.DataFrame(items, index=['pants','book'])
print('b =',b)
c = pd.DataFrame(items, index=['glasses','bike'], columns=['Bob'])
print('c =',c)

# A dict of lists
data2 = {
    'Integers': [1, 2, 3],
    'Floats': [4.5, 8.3, 9.6]
}
d = pd.DataFrame(data2, index=['label1', 'label2', 'label3'])
print('d =',d)

# A list of pyton dicts
items = [
    {'x': 20, 'y': 30, 'z': 140},
    {'x': 20, 'y': 30, 'z': 140, 'pi': 3.14}
]
e = pd.DataFrame(items, index=['Axis1', 'Axis2'])
print('e =',e)
