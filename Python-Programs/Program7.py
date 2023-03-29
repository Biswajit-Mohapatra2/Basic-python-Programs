# PROGRAM 7 :

# Write a Python program to find the average price of cars in a given Toyota.csv dataset using pandas library.

import pandas as pd

df = pd.read_csv('Python-Programs\Toyota.CSV')

avg_price = df['Price'].mean()

print('The average price of the Toyota Cars is:', avg_price)