# Program Number: 03
# Sum Of Digits in Python

# def Sum(n):    
#     sum = 0
#     while (n != 0): 
#          sum = sum + (n % 10)
#          n = n//10
#     return sum    

# num=int(input("Enter the numbers: "))
# print("Sum of digits",Sum(num))

num=int(input("Enter the numbers: "))
sum =0
while num>0:
    i = num%10
    sum = sum + i
    num = num//10

print("Sum Is: ", sum)

# num = int(input("Enter a number: "))
# sum = 0
# for digit in str(num):
#     sum += int(digit)
# print("The sum of digits in", num, "is", sum)


