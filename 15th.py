"""Create a list of 5 names and check given name exist in the List.
        a) Use membership operator (IN) to check the presence of an element.
        b) Perform above task without using membership operator.
        c) Print the elements of the list in reverse direction."""

names = ["hari","krishna","pawan","karan","shital"]

print("checking if pawan exists in list")

#finding using IN operator
given_name = "pawan"
if given_name in names:
    print("pawan exists in list")

#without using IN operator
for x in names:
    if x == given_name:
        print("found name ",given_name)

#printing elements of list in reverse order
for x in reversed(names):
    print(x)
