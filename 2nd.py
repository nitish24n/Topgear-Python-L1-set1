"""Write a program to find the biggest of 3 numbers (Use If Condition)"""

num1 = int(input("first : "))
num2 = int(input("second : "))
num3 = int(input("third : "))

if ((num1 > num2) and (num1 > num3)):
    print (num1," is greatest")
elif ((num2 > num1) and (num2 > num3)):
     print (num2," is greatest")
else: print (num3," is greatest")

