#PROGRAM 1: 

# Using Numpy Create three arrays. Add the elements of first two arrays element wise and store in 3 array. Find the sum and average of 3 array.
import numpy as np

myarr1 = np.array([1, 2, 3, 4, 5, 6])

myarr2 = np.array([7, 8, 9, 10, 11, 12])

myarr3 = myarr1 + myarr2

myarr3_sum = np.sum(myarr3)

myarr3_avg = np.mean(myarr3)

print("Array1:", myarr1)
print("Array2:", myarr2)
print("Array3:", myarr3)
print("Array 3 Sum:", myarr3_sum)
print("Array 3 Average:", myarr3_avg)
