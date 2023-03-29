# PROGRAM 9 :

# What is the Addition of kilometer of the cars from serial number 1 to 10 in the given Toyota.csv dataset? 


import pandas as pd

toyota_df = pd.read_csv('Python-Programs\Toyota.CSV')

filtered_data = toyota_df[toyota_df['id'].between(1, 10)]
total_kms = filtered_data['KM'].sum()

print(f"Total Kilometers of cars with serial number 1 to 10: ", total_kms, "KM")