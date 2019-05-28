"""Create a list with at least 10 elements having integer values in it;
       Print all elements
       Perform slicing operations
       Perform repetition with * operator
       Perform concatenation with other list."""

my_list = [1,2,3,4,5,6,7,8,9,10]

print("all elements of list ")
for x in my_list:
    print (x)

print("slice of top 5 elements of list :",my_list[0:5])

half = int(len(my_list)/2)
print("slice of half elements of list :",my_list[0:half])

print("Python list repititions")
repeat = my_list*2
for x in repeat:
    print (x)

print("concatinating lists l1 and l2")
l1 = [1,2,3,4]
l2 = [5,6,7]
l3 = l1+l2
for x in l3:
    print(x)
