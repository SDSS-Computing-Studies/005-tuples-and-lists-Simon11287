#!python3

"""
Create a variable that contains an empy list.
Ask a user to enter 5 words.  Add the words into the list.
Print the list
inputs:
string 
string
string
string 
string

outputs:
string

example:
Enter a word: apple
Enter a word: worm
Enter a word: dollar
Enter a word: shingle
Enter a word: virus

['apple', 'worm', 'dollar', 'shingle', 'virus']
"""

myList = []
entry = 0
count = 0

while entry !=  1:

    entry = input("Enter a word: ")
    entry  = (entry)
    myList.insert(entry)
    count = count + 1
    if count > 4:
        break

myList.sort()
print(myList)

