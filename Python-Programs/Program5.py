# PROGRAM 5: 

# Using Numpy Create THREE 2-D arrays. Add the elements of first two arrays element wise and store in 3 array. Find the sum and average of 3 array and display the values in this form

# Array 1:

# Row:0   Col :0    Value:

# Row:0   Col :1    Value:

# Row:0   Col :2    Value:

# Row:0   Col :3    Value:

import numpy as np

array1 = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
array2 = np.array([[1, 3, 5], [7, 9, 11], [13, 15, 17]])

array3 = array1 + array2

array3_sum = np.sum(array3)
array3_avg = np.average(array3)

print("# Array 1:")

for i in range(array1.shape[0]):
    for j in range(array1.shape[1]):
        print("Row:{} Col:{} Value:{}".format(i, j, array1[i, j]))

print("\n# Array 2:")

for i in range(array2.shape[0]):
    for j in range(array2.shape[1]):
        print("Row:{} Col:{} Value:{}".format(i, j, array2[i, j]))

print("\n# Array 3:")

for i in range(array3.shape[0]):
    for j in range(array3.shape[1]):
        print("Row:{} Col:{} Value:{}".format(i, j, array3[i, j]))

print("\nSum of Array 3: {}".format(array3_sum))
print("Average of Array 3: {:.2f}".format(array3_avg))
