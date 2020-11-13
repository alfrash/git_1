import pandas as pd
import numpy as np

fruits = pd.Series([10, 6, 3], ['apples', 'oranges', 'bananas'])
print(fruits)
print(fruits + 2)
print(fruits - 2)
print(fruits * 2)
print(fruits / 2)

x = np.sqrt(fruits)
y = np.exp(fruits)
c = np.power(fruits, 2)
print(x,y,c)

print(fruits['bananas'] + 2)
print(fruits.iloc[0] - 1)
print(fruits[['apples', 'oranges']] * 2)
print(fruits.loc[['apples', 'oranges']] / 2)

groceries = pd.Series(data=[30,6,'yes','no'],index=['eggs', 'apples', 'milk', 'bread'])
print(groceries * 2)


distance_from_sun = [149.6, 1433.5, 227.9, 108.2, 778.6]

planets = ['Earth','Saturn', 'Mars','Venus', 'Jupiter']

dist_planets = pd.Series(data = distance_from_sun, index = planets)

time_light = dist_planets / 18

close_planets = time_light[time_light < 40]

print('close_planets =',close_planets)