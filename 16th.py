"""Write program to perform following:
     i) Check whether given number is prime or not.
    ii) Generate all the prime numbers between 1 to N where N is given number.
"""
num = int(input("enter number : "))

#function to check prime condition
def primeCheck(numb):
    isPrime = True
    if (numb == 0 or numb == 1):
        isPrime = False
    else:
        for i in range(2, numb):
            if numb % i == 0:
                isPrime = False
                break
    return isPrime

#outputing result
if primeCheck(num)==True:
    print("number is prime")
else:
    print("number is not prime")

num = int(input("Enter number to find prime numbers in range from 1 till that number : "))

primeList = []
inp = 0

while(inp < num):
    if(primeCheck(inp)):
        primeList.append(inp)
    inp = inp + 1

print("prime no.s between 1 and ",num)
print(primeList)



