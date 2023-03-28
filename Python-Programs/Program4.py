# PROGRAM 4:

# Enter 15 elements to an array from the user and print only -ve elements and sum in python

n = int(input("Enter the number of integers you want to input: "))
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)

negatives = [i for i in arr if i <= 0]
print("Negative elements:", negatives)

sum_of_negatives = sum(negatives)
print("Sum of negative elements:", sum_of_negatives)
