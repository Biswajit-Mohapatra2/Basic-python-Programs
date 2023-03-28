# PROGRAM 2:

# Create an array of 100 elemets, then print  as follows:

# 2,3

# 5,6

# 8,9

# 11,12

# 14,15

array = list(range(1, 101))

for i in range(1, len(array), 3):
    print(f"{array[i]}, {array[i+1]}")