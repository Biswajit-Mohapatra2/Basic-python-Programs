#Program Number: 04
# Check a Number Is Palindrome or not

num = int(input("Enter Your Number: "))
temp = num
reverse = 0
while temp > 0:
    remainder = temp % 10
    reverse = (reverse * 10) + remainder
    temp = temp // 10
if num == reverse:
  print('This is a Palindrome Number')
else:
  print("This Is Not a Palindrome Number")