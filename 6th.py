"""Write a program to read string and print each character separately.
    a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
    b) Repeat the string 100 times using repeat operator *
    c) Read string 2 and concatenate with other string using + operator.
"""

input_string = input("Enter a string : ")

# printing each character separately

for x in range(0, len(input_string)):
    print(input_string[x])

slice_string = input_string[0:5]
print("sliced string : ", slice_string)

repeat_string = slice_string*100
print("100 times repeat string : ", repeat_string)

string_two = input("Enter second string : ")
print("concatinated strings : ", input_string+string_two)
