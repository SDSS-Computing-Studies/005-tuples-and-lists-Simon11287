#! python3
"""
Sort the given list by numerical value
Find the smallest and the largest value and display them:

inputs:
none

outputs:
string containing the 2 numbers:

example:
The smallest number is 3 and the largest number is 9
"""

myList = [ 3,6,5,4,6,7,8,6,5,9,4,5 ]
myList = [ 3,6,5,4,6,7,8,6,5,9,4,5 ]
print(myList)
myList.sort()
print(myList)
dCount = myList.count("3")
print("The number of times the number 3 appears is :" + str(dCount))
dCount = myList.count("9")
print("The number of times the number 9 appears is :" + str(dCount))
