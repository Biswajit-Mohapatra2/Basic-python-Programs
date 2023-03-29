# PROGRAM 6:

# Write a Python program to find the cheapest and most expensive products in a given Toyota.csv dataset.

import pandas as pd

df = pd.read_csv('Python-Programs\Toyota.CSV')

cheapest_product = df.loc[df['Price'].idxmin()]
most_expensive_product = df.loc[df['Price'].idxmax()]

print('The cheapest product is:')
print(cheapest_product)
print('\nThe most expensive product is:')
print(most_expensive_product)