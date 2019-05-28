"""Write a program to find the biggest of 4 numbers.
   a) Read 4 numbers from user using Input statement.
   b) extend the above program to find the biggest of 5 numbers.
(PS: Use IF and IF & Else, If and ELIf, and Nested IF)"""

first,second,third,forth = input().split()
first,second,third,forth = int(first),int(second),int(third),int(forth)

biggest = first
if second > biggest:
    biggest = second
if third > biggest:
    biggest = third
if forth > biggest:
    biggest = forth

print("biggest of four numbers is ",biggest)

a,b,c,d,e = input().split()
a,b,c,d,e = int(a),int(b),int(c),int(d),int(e)


biggest2 = a
if b > biggest2:
    biggest2 = b
if c > biggest2:
    biggest2 = c
if d > biggest2:
    biggest2 = d
if e > biggest2:
    biggest2 = e

print("biggest of five numbers is ",biggest2)
