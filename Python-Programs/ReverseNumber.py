n = int(input("Enter Your Number: "))

reverse = 0

while n!=0:
    i = n%10
    reverse = reverse * 10 + i
    n = n // 10

print("The Reverse Number is: ", reverse)