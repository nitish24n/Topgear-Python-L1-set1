"""
Using loop structures print even numbers between 1 to 100. 
a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
    i) Break the loop if the value is 50
    ii) Use continue for the values 10,20,30,40,50
"""

for i in range(1,100):
    if i % 2 != 0:
        pass
    if i % 2 == 0:
        if i == 50:
            break
        if i in [10,20,30,40,50]:
            continue
        print(i)


# b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
#     i) Break the loop if the value is 90
#     ii) Use continue for the values 60,70,80,90
j = 0
while j < 100:
    j = j + 1
    if j % 2 != 0:
        pass
    if j % 2 == 0:
        if j == 90:
            break
        if j in [60,70,80,90]:
            continue
        print(j)
