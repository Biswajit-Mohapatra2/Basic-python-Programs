# Print the number and their square roots from 1 to 10 in python

from math import sqrt

for i in range(1, 11):
    square_root = sqrt(i)
    print(f"The Square Root Of {i} is: ", square_root)
