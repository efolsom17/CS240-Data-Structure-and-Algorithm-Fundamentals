# Data Structures Assignment 1 - Eric Folsom #
##############################################

# Reading the data used to verify implementation

with open("./Data/numbers-2.txt", "r") as nums: #opens the file
    numbers2 = [int(line.strip()) for line in nums] #extract contents line by line and store as an integer.

## Smaller list of numbers to test with before I implement the full numbers-2.txt data.
numbers_test = list(range(0,100)) # need to make sure to define as a list, python doesnt do this automatically like R does.



# Implementing a singly linked list in python.