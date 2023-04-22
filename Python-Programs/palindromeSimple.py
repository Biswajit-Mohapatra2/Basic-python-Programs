n = int(input("Enter Your Number: "))
palindrome =0 

while n>0:
    r = n%10
    palindrome = (palindrome * 10) + r
    n = n/10
if n == palindrome:
    print("Palindrome Number")
else:
    print("Not a palindrome Number")