"""Repeat program 7 with Tuples (Take example from Tutorial)"""

my_tuple = (1,2,3,4,5,6,7,8,9,10)

print("all elements of tuple ")
for x in my_tuple:print (x)

print("slice of top 3 elements of tuple :",my_tuple[0:3])

half = int(len(my_tuple)/2)
print("slice of half elements of list :",my_tuple[0:half])

print("Python tuple repititions")
repeat = my_tuple*2
for x in repeat:print (x)

print("concatinating tuples l1 and l2")
l1 = (1,2,3,4)
l2 = (5,6,7)
l3 = l1+l2
for x in l3:print(x)
