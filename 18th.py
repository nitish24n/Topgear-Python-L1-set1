
"""
Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)
a) By using For loop
b) By using while loop
c) Let mystring ="Hello world"
print each character of mystring in to separate line using appropriate loop
"""

#for-loop 1 to 100
for i in range(1,101):
    print(i)
#reversed order
for i in range(100,0,-1):
    print(i)

#while -loop 1 to 100
i = 1
while i <= 100:
    print(i)
    i = i +1
#reversed order
i = 100
while i >= 1:
    print(i)
    i = i -1

#printing all characters in seperate line
mystring ="Hello world"
for i in mystring:
    print(i)
