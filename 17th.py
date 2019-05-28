"""Write program to find the biggest and Smallest of N numbers.
      PS: Use the functions to find biggest and smallest numbers. """

inp = int(input("Enter the no of elements you want : "))
myList = []
for i in range(0,inp):
    myList.append(int(input("->")))

print("biggest number is ",max(myList))
print("smallest number is ",min(myList))
