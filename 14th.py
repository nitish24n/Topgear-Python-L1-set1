"""Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list) & perform following operation"""

listA = [45,1,92,36,45,53,62,17,8,9]
listB = ["arya","sansa","john","harry","khalese","khal","drogo","stanis","martha","suman"]

#       a) Print all names on to screen
for i in listB:
    print(i)

#       b) Read the index from the  user and print the corresponding name from both list.
index = int(input("enter index : "))
print("index",index,"has id=",listA[index],"and name=",listB[index])

#       c) Print the names from 4th position to 9th position
for i in range(4,10):
    print("name at position",i,"is",listB[i])
#print(listB[4:10])

#       d) Print all names from 3rd position till end of the list
for i in range(3,len(listB)):
    print("name at position",i,"is",listB[i])
#print(listB[3:])

#       e) Repeat list elements by specified number of times (N- times, where N is entered by user)
repeat = int(input("enter the no of times you want list to be repeated :"))
print("repeated list : ",listB*repeat)

#     f)  Concatenate two lists and print the output.
print("concatinating lists : ",listA+listB)

#     g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )
for i in range(0,len(listB)):
    print(listA[i],listB[i])
