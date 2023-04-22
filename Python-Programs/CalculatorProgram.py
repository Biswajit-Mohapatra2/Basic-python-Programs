num1 = float(input("Enter your First Number:"))
Operator = input("Enter your Operator: ")
num2 = float(input("Enter Your Second Number: "))

if Operator == "+":
    print("The answer is: ", (num1 + num2))
elif Operator == "-":
    print("The answer is: ", (num1 - num2))
elif Operator == "*":
    print("The answer is: ", (num1 * num2))
elif Operator == "/":
    print("The answer is: ", (num1 / num2))
else:
    print("Invalid Number You Entered..")