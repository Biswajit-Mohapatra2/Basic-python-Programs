# Program Number: 03
# Sum Of Digits in Python

def Sum(n):    
    sum = 0
    while (n != 0): 
         sum = sum + (n % 10)
         n = n//10
    return sum    

num=int(input("Enter the numbers: "))
print("Sum of digits",Sum(num))
