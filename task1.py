#!python3

"""
Create a list that contains the following strings, in order:
Cat
Fish
Dog
Bear
Turtle

Sort the list into alphabetical order and and then ask the user to enter a number corresponding
to the index of an element.  Print the element associated with that index.

inputs:
integer number

outputs:
string animal

example:
Enter the index for an animal:2
The animal at that index is Dog
"""



animals =
myList = ['Cat', 'Fish', 'Dog', 'Bear', 'Turtle']
print(myList)
myList.sort()
print(myList)
print("\n")
dIndex = myList.index("Dog")
print("Dog is found at index " + str(dIndex) + " using myList.index('Dog') ")
