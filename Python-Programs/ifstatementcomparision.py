def maxnum(num1, num2, num3):
    if num1 >=num2 and num1 >= num3:
        print("The Greatest Is: " + str(num1))
    elif num2>=num1 and num2>=num3:
        print("The Biggest is: " + str(num2))
    else:
        print("The Greatest Number is: " + str(num3))
maxnum(3, 40, 5)