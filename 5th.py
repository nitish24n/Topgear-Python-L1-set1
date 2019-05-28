"""Write a program to receive 5 command line arguments and print each argument separately.
Example: >> python test.py arg1 arg2 arg3 arg4 arg5
a) From the above statement your program should receive arguments and print them each of them.
b) Find the biggest of three numbers, where three numbers are passed as command line arguments.
"""

import sys

print("printing all command line args")
for x in range(len(sys.argv)):
    print(sys.argv[x])


# if three numbers are provided in command line args
if len(sys.argv) == 4:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    num3 = int(sys.argv[3])

    if(num1 > num2) and (num1 > num3):
        print(num1, " is greatest")
    elif(num2 > num1) and (num2 > num3):
        print(num2, " is greatest")
    else:
        print(num3, " is greatest")
