"""Read 10 numbers from user and find the average of all.
a) Use comparison operator to check how many numbers are less than average and print them
b) Check how many numbers are more than average.
c) How many are equal to average."""
inputList = []
for i in range(10):
    inputList.append(int(input("enter number : ")))

sum = 0
for i in inputList:
    sum = sum + i

avg = sum/len(inputList)
print("average : ",avg)
equalToAvg = 0
lessThanAvg = 0
moreThanAvg = 0
for i in inputList:
    if i <  avg:
        print(i," is less than avg")
        lessThanAvg = lessThanAvg + 1
    elif i >  avg:
        print(i," is more than avg")
        moreThanAvg = moreThanAvg + 1
    else:
        print(i," is equal to avg")
        equalToAvg = equalToAvg + 1


print(lessThanAvg," numbers are less than avg")
print(moreThanAvg," numbers are more than avg")
print(equalToAvg," numbers are equal to avg")

