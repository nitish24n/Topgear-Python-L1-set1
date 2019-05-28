"""Write a program to find the number is Prime or not."""

num = int(input("Enter a number : "))

isPrime = True

if(num == 0 or num == 1):
    isPrime = False
    
else:
    for x in range(2,num):
        #print (x, "  ", isPrime)
        if num % x == 0:
            isPrime = False
            break
          


if (isPrime == True):
    print("prime number")
else:
    print("not a prime number")


