# Data Structures Assignment 1 - Eric Folsom #
##############################################

# Reading the data used to verify implementation

with open("./Data/numbers-2.txt", "r") as nums: #opens the file
    numbers2 = [int(line.strip()) for line in nums] #extract contents line by line and store as an integer.

## Smaller list of numbers to test with before I implement the full numbers-2.txt data.
numbers_test = list(range(0,100)) # need to make sure to define as a list, python doesnt do this automatically like R does.


# Implementing a singly linked list in python.


# Head  ##
#  contains the data of the first node



class Node: # Houses data and the pointer for the next position
    def __init__(self, item): #initializing the node
        self.data = item # data contained in the node for this case gonna be an int to be simple
        self.next = None # Go to the next node, making None as the default value for next.
        self.prev = None # Go to the previous node, making None as the default value for prev. 
        
## Hoping I don't have to create a new node if 
        
# Okay we have a node now we can make the linked list
# I think

class SingleLinkedList: # This should hopefully convert a typical list to a linked list when running SingleLinkedList() on a list
    # such as x = [1,2,3,4], doing SingleLinkedList(x) would convert the list to a single linked list.
    def __init__(self, data):
        self.head = None
        if isinstance(data, list):
            self.data = data

# Read ## 

## beginning  ## 

## random position ##

## end ##

# Insert ## 

## beginning ## 

## random position ##

## end ##

# Delete ##

## beginning ## 

## random position ##

## end ##

# Linear Search ##

# Sort ##

## Selection Sort ##

## Insertion Sort ##

#### Implementing a doubly-linked list in Python

# Head  ##


# Node ##

## Data  ##

## Next  ##

## previous ##

# Read ## 

## beginning  ## 

## random position ##

## end ##

# Insert ## 

## beginning ## 

## random position ##

## end ##

# Delete ##

## beginning ## 

## random position ##

## end ##

# Linear Search ##

# Sort ##

## Selection Sort ##

## Insertion Sort