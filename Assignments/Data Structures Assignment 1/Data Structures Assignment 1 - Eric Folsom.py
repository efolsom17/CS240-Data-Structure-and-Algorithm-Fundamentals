# Data Structures Assignment 1 - Eric Folsom #
##############################################

# Reading the data used to verify implementation

with open("./Data/numbers-2.txt", "r") as nums: #opens the file
    numbers2 = [int(line.strip()) for line in nums] #extract contents line by line and store as an integer.

## Smaller list of numbers to test with before I implement the full numbers-2.txt data.
numbers_test = list(range(0,100)) # need to make sure to define as a list, python doesnt do this automatically like R does.

## So I can randomly sample indices of the data, importing them so that they have the same function names as in R.
from random import randint as rdunif # random integer from a discrete uniform distribution
from random import uniform as runif # random number from a uniform distribution
from random import gauss as rnorm # random number from a normal (gaussian) distribution
from random import seed as set_seed # setting a random seed, in R this is set.seed(), had to use _ here in python
from random import sample as sample # for randomizing numbers_test

#setting a random seed for reproducability.
set_seed(12345)

# random order, for testing sorting

numbers_test2 = list(sample(range(100), 100))

# Implementing a singly linked list in python.


# Head  ##
#  contains the data of the first node
'''

 Okay I think the node is the important part of this. once I have the node I can just start to code.
 beginning to get an idea of what I am trying to do. 
 
 Start with building a node. Then all a linked list is a list where each item in the list is a node that points to the next node.
 So to do this, I need to make a single linked list class that when invoked, similar to how int() or how float() works but on a list, will
 turn every item in a list into a node and then connect the nodes. and then be able to implemment the other requirements
 
 The example from the readings on canvas created a linked list when you ran the python script. I want to create the linked list when you call singleLinkedList(obj)  
'''

class Node: # Houses data and the pointer for the next position
    def __init__(self, item): #initializing the node
        self.data = item # data contained in the node for this case gonna be an int to be simple
        self.next = None # Go to the next node, making None as the default value for next.
        self.prev = None # Go to the previous node, making None as the default value for prev. 
        
## Hoping I don't have to create a new node if 
        
# Okay we have a node now we can make the linked list
# I think



class SinglyLinkedList: 
    
    ## Initializing the linked list class.
    # This should hopefully convert a typical list to a linked list when running SingleLinkedList() on a list
    # such as x = [1,2,3,4], doing SingleLinkedList(x) would convert the list to a single linked list.
    
    def __init__(self, data):
        self.head = None # Set the head to be None
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
            self.list_length = int(len(data)) # will be needed later for randomization stuff. stores the length of the input list
        else:
            raise TypeError("Expected a list") # ensure that the data is a list
        
        
       ### Read #### 
    def read(self, beg = False, rand = False, end = False, node= int):
        from random import randint as rdunif # random integer from a discrete uniform distribution
        if beg == True: # Beginning
            print(self.head.data) # print the data in the head node
        elif rand == True: #random node
            rand_index = rdunif(0, self.list_length-1) # select a random index
            current = self.head # assign the head to be the current node we are at
            index_counter = 0 # To keep track of the index we are at
            while index_counter <= rand_index: # while we have not reached the index we are looking for
                node_data = int(current.data) # store the data of the current node we are at
                current = current.next # go to the next node
                index_counter += 1 # increment the counter to be the index we are searching for
            return print(f"We are reading the data at index: {rand_index} which contains {node_data}.")      
        elif end == True: # end of the linked list  
            current = self.head # assign the head to be the current node we are at
            while current: # while current \neq None
                node_data = int(current.data) # store the data of the current node we are at.
                current = current.next# go to the next node
            return print(node_data)
        elif node >= self.list_length: # if specified node is not within the bounds
            return print(f"Index Out of Bounds")
        else: # if we specify the node to read
            current = self.head # start at the beginning of the list
            index_counter = 0 # self explanitory
            while index_counter <= node: # while we have not reached the node that we want to be in stop once we reach it
                node_data = int(current.data) # store the data of the node (might be able to move this outside of the while loop, after testing I cannot)
                current = current.next
                index_counter += 1           
            return print(f"The data contained in Node {node} is {node_data}.")
                
    # insert #
    def insert(self, beg = False, rand = False, end = False, data = any):
        from random import randint as rdunif # random integer from a discrete uniform distribution
        new_node = Node(data)     # Assign the data (value) of the new node, where new_node.next = None
        if beg == True:
            new_node.next = self.head # Point the next part of the new node to the head node
            self.head = new_node # assign the new node as the head of the linked list   
        elif rand == True:
            rand_index = rdunif(0, self.list_length-1) # select a random index
            current = self.head # Start at the head of the list
            index_counter = 0 # storing the current index
            while index_counter < rand_index-1: # Traverse the list until we have reached one less than the randomly sampled index.
                current = current.next # go to the next node (the index we sampled)
                index_counter += 1 #update what node we are in (for printing the index we inserted the value into)
            new_node.next = current.next # once we have reached the node before we want to insert a new node at, then replace the next pointer 
            current.next = new_node # and point the current node to the new node we inserted.
            return print(f"We have inserted the value {data} at node {index_counter}")
        elif end == True:
            current = self.head    # Start at the beginning of the list
            while (current.next): # while current.next \neq None
                current = current.next # go to the next node (traverse the list)
            current.next = new_node # once current.next == None, point the last node to the new node we created earlier. 
        self.list_length += 1 # update the length of the linked list (add one node to the length)  
    
    def delete(self, beg = False, rand = False, end = False):
        from random import randint as rdunif # random integer from a discrete uniform distribution
        if beg == True: # if we are deleting from the beginning of the list (head)
             self.head = self.head.next # re-assign the head to be the next node
             self.list_length -= 1 # update the legnth of the list (one smaller).
        elif rand == True: # if we are deleting a random node
            rand_index = rdunif(0, self.list_length-2)# select A random index, excluding the last node
            current = self.head # start at the beginning of the list
            for _ in range(rand_index): # traverse through the list rand_index times, ChatGPT reccomended this as being more elegant than my while loop used in insertion. _ is a placeholder dummy variable that will node be used, basically says do whats inside the for loop rand_index number of times.
                current = current.next # go to the next node. we do this rand_index times
                node_data = current.next.data # storing this so we can tell the user what node and data we actually deleted.
            current.next = current.next.next if current.next else None  # Skip the node at the random index. Point the node from the node before the random index to the node after the random index.
            self.list_length -= 1 # update the legnth of the list (one smaller).
            print(f"We have deleted node {rand_index+1} which contained the value {node_data}")
        elif end == True: # if we are deleting from the end of the linked list (last node)  
            
            if self.head is None: # Check if the linked list is empty
                return "List is empty"  # If there's no node to delete

            if self.head.next is None: # check if the linked list has only one node (the head)
                self.head = None  # If there's only one node, remove it
                self.list_length -= 1 # update the length of the linked list.
                return
            
            current = self.head # start at the beginning of the list
            while current.next.next: #while current.next.next \neq None
                current = current.next # go to the next node, will eventually reach the second to last node in the linked list
            current.next = None # delete the pointer to the last node in the linked list
            self.list_length -= 1 # update the legnth of the list (one smaller).
    def search(self, value):
        current = self.head # assign the head to be the current node we are on
        node_count = 0
        while current: # while current \neq None
            if current.data == value: # if we find the item we are searching for
                return print(f"{value} is located at node {node_count}") # print the value and the index of it
            else:
                node_count += 1 # increment the index we are at
                current = current.next # go to the next node
                
        return print(f"Item Not found. This took {node_count} searches.") # if the item isn't found tell us how many searches it took.
    
    def sort(self, asc = True, desc = False): # going to be selection sort
        if desc == True: # if we want to sort the list in descending order
            current = self.head # start at the beginning of the list
            while current: # while current \neq none, outer loop, current is the unsorted part of the list
                max_node = current # asssume that the first unsorted element is the maximum value in the list $x_i$
                search = current.next # the value we are comparing x_i to x_j
                while search: # while search \neq None
                    if search.data > max_node.data:
                        max_node = search
                    search = search.next
                # swap the data of the current node with the data of max_node
                current.data, max_node.data = max_node.data, current.data
                current = current.next # go to the next node and compare
        else: # if we want to sort the list in ascending order (default when you call .sort())
            current = self.head # start at the beginning of the list
            while current: # while current \neq none, outer loop, current is the unsorted part of the list
                min_node = current # asssume that the first unsorted element is the minimum value in the list $x_i$
                search = current.next # the value we are comparing x_i to x_j
                while search: # while search \neq None
                    if search.data < min_node.data:
                        min_node = search
                    search = search.next
                # swap the data of the current node with the data of min_node
                current.data, min_node.data = min_node.data, current.data
                current = current.next # go to the next node and compare
        
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
        return " -> ".join(nodes) #print the linked list, with nodes connected with an arrow.



#### Implementing a doubly-linked list in Python

class DoublyLinkedList:
    #initializing doubly linked list
    def __init__(self, data):
        self.head = None # start of the linked list
        self.tail = None # end of the linked list, so we can traverse the list starting from the other end of the list.
        if isinstance(data, list): #ensuring that the input data is a list
            self.head = Node(data[0]) # assign the first index of the list as the head
            current = self.head # start at the beginning of the list
            for item in data[1:]: # for every other index of the input array or list
                new_node = Node(item) # creates a new node with the data of the input list 
                new_node.prev = current # point the new node to the previous node
                current.next = new_node # point the previous node to the new node
                current = new_node # go to the next node
            self.tail = current # The current node is at the end of the list so assign it as such.
            self.list_length = len(data) # will be needed later for some randomization stuff.
        else:
           raise TypeError("Expected a list") # ensure that the inputted data is a list 
        
    # Read ## 
    def read(self, beg = False, rand = False, end = False, node= int):
        from random import randint as rdunif # random integer from a discrete uniform distribution
        if beg == True:
            return print(self.head.data) #read the head
        elif end == True:
            return print(self.tail.data) #read the tail
        elif rand == True:
            rand_index = rdunif(0,self.list_length-1) # select a random node
            current = self.head # start at the beginning of the list
            for _ in range(rand_index): # repeat this until we reach the random node
                current = current.next # go to the next node
            return print(f"We are reading the data at node {rand_index}, which contains: {current.data}")
        elif node >= self.list_length: # if specified node is not within the bounds
            return print(f"Index Out of Bounds")
        else:
            current = self.head # start at the beginning of the list
            index_counter = 0 # self explanitory
            while index_counter <= node: # while we have not reached the node that we want to be in stop once we reach it
                node_data = int(current.data) # store the data of the node (might be able to move this outside of the while loop, after testing I cannot)
                current = current.next
                index_counter += 1           
            return print(f"The data contained in Node {node} is {node_data}.") 
    
    # insert #
    def insert(self, beg = False, rand = False, end = False, data = any):
        from random import randint as rdunif # random integer from a discrete uniform distribution


    # Delete ##

    def delete(self, beg = False, rand = False, end = False):
        from random import randint as rdunif # random integer from a discrete uniform distribution
        pass

    # Linear Search ##
    def search(self, value):
        pass

    # Sort, insertion sort ##
    def sort(self, asc = True, desc = False):
        pass
    
    # Printing methods, ChatGPT was my friend for this one. identical to singly linked list, except for <-> instead of -> 
    # to represent that each node is linked to the next node and the previous node instead of just the next node.
    def __repr__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(repr(current.data))
            current = current.next
        return " <-> ".join(nodes)

    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " <-> ".join(nodes)   