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
'''

 Okay I think the node is the important part of this. once I have the node I can just start to code.
 beginning to get an idea of what I am trying to do. 
 
 Start with building a node. Then all a linked list is a list where each item in the list is a node that points to the next node.
 So to do this, I need to make a single linked list class that when invoked, similar to how int() or how float() works but on a list, will
 turn every item in a list into a node and then connect the nodes. and then be able to implemment the other requirements
 
 The example from the readings on canvas created a linked list when you ran the python script. I  
 
'''

class Node: # Houses data and the pointer for the next position
    def __init__(self, item): #initializing the node
        self.data = item # data contained in the node for this case gonna be an int to be simple
        self.next = None # Go to the next node, making None as the default value for next.
        self.prev = None # Go to the previous node, making None as the default value for prev. 
        
## Hoping I don't have to create a new node if 
        
# Okay we have a node now we can make the linked list
# I think

# function to build nodes from a list of integers.

'''
FOR SINGLE LINKED LIST

1. assign node 1 to index 0
    nvm doing this as a class method is better than this.

'''

def build_node_single(data = list):
    pass


def build_node_double(data = list):
    pass

class SingleLinkedList: # This should hopefully convert a typical list to a linked list when running SingleLinkedList() on a list
    # such as x = [1,2,3,4], doing SingleLinkedList(x) would convert the list to a single linked list.
    def __init__(self, data):
        self.head = None
        if isinstance(data, list): # from chatGpT, ensures that you are transforming an array/list.
            self.head = Node(data[0])
            print(self.head.data)
            current = self.head
            print(current.data)
            for item in data[1:]:
                current.next = Node(item)
                print(current.next.data)
                current = current.next
                print(current.data, current.next)
        else:
            raise TypeError("Expected a list")
        
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