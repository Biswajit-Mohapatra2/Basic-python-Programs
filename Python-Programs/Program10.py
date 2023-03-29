# PROGRAM 10 :

#  Display Replace all the value of the column 'MetColor' 1 to 3 and all the values in 'MetColor' 0 to 4 in the given Toyota.csv dataset in python.

import pandas as pd

df = pd.read_csv("Python-Programs\Toyota.CSV")

df['MetColor'] = df['MetColor'].replace({1:3, 0:4})

df.to_csv("Toyota_updated.csv", index=False)
print(df)
