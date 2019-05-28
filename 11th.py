"""Read 2 numbers to variable a and b and perform all bitwise operations on that numbers."""

first = int(input("enter first : "))
second = int(input("input second : "))

print("AND operator x & y =",first & second)
print("OR operator x | y =",first | second)
print("NOT operator ~x =",~first)
print("XOR operator x ^ y =",first ^ second)
print("Right shift >> =",first>>3)
print("Left shift << =",first<<3)
