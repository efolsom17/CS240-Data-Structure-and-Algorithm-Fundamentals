# Data Structures Assignment 1 - Eric Folsom #
##############################################

# Reading the data used to verify implementation

with open("./Data/numbers-2.txt", "r") as nums: #opens the file
    numbers2 = [int(line.strip()) for line in nums] #extract contents line by line and store as an integer.

## Smaller list of numbers to test with before I implement the full numbers-2.txt data.
numbers_test = list(range(0,100)) # need to make sure to define as a list, python doesnt do this automatically like R does.

## So I can randomly sample indices of the data, importing them so that they have the same function names as in R.
from random import randint  as rdunif # random integer from a discrete uniform distribution
from random import uniform as runif # random number from a uniform distribution
from random import gauss as rnorm # random number from a normal (gaussian) distribution
from random import seed as set_seed

#setting a random seed for reproducability.
set_seed(12345)


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



class SingleLinkedList: 
    
    ## Initializing the linked list class.
    # This should hopefully convert a typical list to a linked list when running SingleLinkedList() on a list
    # such as x = [1,2,3,4], doing SingleLinkedList(x) would convert the list to a single linked list.
    
    def __init__(self, data):
        self.head = None # Set the head to be None
        self.list_length = int(len(data)) # will be needed later for randomization stuff. stores the length of the input list
        if isinstance(data, list): # from chatGpT, ensures that you are transforming an array/list.
            self.head = Node(data[0]) # Assign the head of the linked list to be index 0 of the input array or list
            #print(self.head.data)
            current = self.head # Assign head to be the current node containing the data of index 0 of the input
            #print(current.data)
            # the below for loop assigns each remaining index as a node in the linked list 
            # and then points that node to the next node until we run out of indices to assign.
            for item in data[1:]: # for every other index of the input array or list
                current.next = Node(item) # Assign the next node to contain the data of the current index in the for loop
                #print(current.next.data)
                current = current.next # Set the next node to be the current node (go to the next node)
                #print(current.data)
        else:
            raise TypeError("Expected a list")
        
        
       ### Read #### 
    def read(self, beg = False, rand = False, end = False, node= int):
        if beg == True:
            print(self.head.data) # print the data in the head node
        elif rand == True:
            rand_index = rdunif(0, self.list_length-1) # select a random index
            #print(rand_index)
            current = self.head # assign the head to be the current node we are at
            #print(current.data)
            index_counter = 0 # To keep track of the index we are at
            while index_counter <= rand_index: # while we have not reached the index we are looking for
                #print(f"Current Node Data: {current.data}")
                #print(f"Current Node: {index_counter}")
                #print(f"The next node contains: {current.next.data}")
                node_data = int(current.data) # store the data of the current node we are at
                current = current.next # go to the next node
                index_counter += 1 # increment the counter to be the index we are searching for
                #print(f"The next node is: {index_counter}")
            return print(f"We are reading the data at index: {rand_index} which contains {node_data}.")
                
        elif end == True:   
            current = self.head # assign the head to be the current node we are at
            while current: # while current \neq None
                node_data = int(current.data) # store the data of the current node we are at.
                current = current.next# go to the next node
            return print(node_data)
        elif node >= self.list_length:
            return print(f"Index Out of Bounds")
        else:
            current = self.head
            index_counter = 0
            while index_counter <= node:
                node_data = int(current.data)
                current = current.next
                index_counter += 1
            return print(f"The data contained in Node {node} is {node_data}.")
                

    def insert(self, beg = False, rand = False, end = False, data = any, node = int):
        if beg == True:
            new_node = Node(data)     # Assign the data (value) of the new node
            new_node.next = self.head # Point the next part of the new node to the head node
            self.head = new_node # assign the new node as the head of the linked list   
        elif rand == True:
            new_node = Node(data)     # Assign the data (value) of the new node
            rand_index = rdunif(0, self.list_length-1) # select a random index
            print(rand_index)
            current = self.head # Start at the head of the list
            index_counter = 0 # storing the current index
            while index_counter < rand_index-1: # Traverse the list until we have reached the randomly sampled index.
                current = current.next # go to the next node
                index_counter += 1 #update what node we are in
            new_node.next = current.next
            current.next = new_node
            return print(f"We have inserted the value {data} at index {index_counter}")
        elif end == True:   
            pass
    
    def delete(self, beg = False, rand = False, end = False, node = None):
        if beg == True:
            pass
        elif rand == True:
            pass
        elif end == True:   
            pass
    
    def search(self, value):
        current = self.head # assign the head to be the current node we are on
        index_count = 0
        while current: # while current \neq None
            if current.data == value: # if we find the item we are searching for
                return print(f"{value} is located at index {index_count}") # print the value and the index of it
            else:
                index_count += 1 # increment the index we are at
                current = current.next # go to the next node
                
        return print(f"Item Not found. This took {index_count} searches.") # if the item isn't found tell us how many searches it took.
    
    def sort(self):
        pass
        
    # Allow us to print/visualize the list if it is called like linkedlist(obj) 
    def __repr__(self):
        nodes = [] # list of nodes
        current = self.head # Assign the current node to be the head
        while current: # while current \neq None, will equal None if at the end of the Linked List 
            nodes.append(repr(current.data)) # add the current data of the linked list to the list of nodes
            current = current.next # go to the next node
        return " -> ".join(nodes) # returns the linked list printed with the values being joined with an arrow
    
    # Allow us to print/visualize the list if it is called using print()
    def __str__(self):
        nodes = [] # list of nodes
        current = self.head # set the head of the node to be the current node
        while current: # while current \neq None
            nodes.append(str(current.data)) # add the data of the node as a string
            current = current.next # go to the next node
        return "Linked list contains: " + " -> ".join(nodes) #print the linked list, with nodes connected with an arrow.



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