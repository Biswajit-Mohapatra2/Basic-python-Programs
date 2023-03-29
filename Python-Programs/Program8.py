# Program 8 :

# Display the 3rd to 6th columns of the rows from 100 too 200 in the Toyota.csv file using pandas library in python

import pandas as pd

df = pd.read_csv("Python-Programs\Toyota.CSV")

result = df.iloc[100:201, 2:6]

print(result)
