#!python3
"""
Print the list named "people"
Ask the user to enter a word from the list
Ask the user to enter another word
Replace the first word with the second word.

inputs:
string
string

outputs:
list

example:
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Rick']
Choose a person from the list to replace:Rick
Enter the replacement:Dan
['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']

"""
myList = ['Alain', 'Brian', 'Chris', 'Justin', 'Angela', 'Dan']
print(myList)

myList.remove( input("enter a name from the list: "))
print(myList)

myList.insert(0, input("enter a word to replace"))
print(myList)
