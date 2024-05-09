class Node: # Houses data and the pointer for the next position
    def __init__(self, item): #initializing the node
        self.data = item # data contained in the node for this case gonna be an int to be simple
        self.next = None # Go to the next node, making None as the default value for next.
        self.prev = None # Go to the previous node, making None as the default value for prev. 
        


class SingleLinkedList: 
    
    ## Initializing the linked list class.
    
    def __init__(self, data):
        self.head = None # Set the head to be None
        if len(data) == 0:
            self.list_length = 0
        elif isinstance(data, list): # from chatGpT, ensures that you are transforming an array/list.
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
    def insert(self, data = any, beg = False, rand = False, end = False):
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
    # Delete
    def delete(self,value, beg = False, rand = False, end = False):
        from random import randint as rdunif # random integer from a discrete uniform distribution
        if bool(value) == True: # if there was an input for value, delete a specific value from the linked list.
            current = self.head
            prev = None
            while current:
                if current.data == value:
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                    return True
            prev = current
            current = current.next
            self.list_length -= 1
            return False
        
        elif beg == True: # if we are deleting from the beginning of the list (head)
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
    #Search
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
    #selection Sort
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



#### Implementing a double-linked list in Python

class DoubleLinkedList:
    #initializing double linked list
    def __init__(self, data):
        self.head = None # start of the linked list
        self.tail = None # end of the linked list, so we can traverse the list starting from the other end of the list.
        if len(data) == 0:
            self.list_length = 0
        elif isinstance(data, list): #ensuring that the input data is a list
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
        if beg:
            return self.head.data #read the head
        elif end:
            return self.tail.data #read the tail
        elif rand:
            rand_index = rdunif(0,self.list_length-1) # select a random node
            current = self.head # start at the beginning of the list
            for _ in range(rand_index): # repeat this until we reach the random node
                current = current.next # go to the next node
            return f"We are reading the data at node {rand_index}, which contains: {current.data}"
        elif node >= self.list_length: # if specified node is not within the bounds
            return print(f"Index Out of Bounds")
        else:
            current = self.head # start at the beginning of the list
            index_counter = 0 # self explanitory
            while index_counter <= node: # while we have not reached the node that we want to be in stop once we reach it
                node_data = int(current.data) # store the data of the node (might be able to move this outside of the while loop, after testing I cannot)
                current = current.next
                index_counter += 1           
            return f"The data contained in Node {node} is {node_data}." 
    
    # insert #
    def insert(self, data=any, beg=False, rand=False, end=False):
        from random import randint as rdunif  # random integer from a discrete uniform distribution
        new_node = Node(data)  # create a new node with the data, prev = None and next = None
        if beg:  # if beg == True, we are inserting at the beginning
            new_node.next = self.head  # point the new node to the head
            if self.head:  # if the linked list already has a head assigned (if the list isn't empty it will)
                self.head.prev = new_node  # point the head node to the previous node (the new one we are inserting)
            self.head = new_node  # assign our new node as the head.
            if self.tail is None:  # if it's the first node being added
                self.tail = new_node  # also set it as tail
        elif end:  # if end == true, we are inserting at the end
            new_node.prev = self.tail  # point the new node prev to the tail of the list
            if self.tail:  # does a tail already exist (if the list is not empty then yes)
                self.tail.next = new_node  # point the tail to the new node, assign next to be new node
            self.tail = new_node  # set the new node as the tail
            if self.head is None:  # if the list is empty
                self.head = new_node  # set the new node as the head (technically at the end of the list)
        elif rand:  # if rand == true, inserting at a random node
            if self.list_length == 0:  # if the list is empty 
                self.head = new_node
                self.tail = new_node
            else:
                rand_index = rdunif(0, self.list_length-1)  # select a random index
                current = self.head  # start at the beginning of the linked list
                index_counter = 0 #so we know which index we inserted the data into
                for _ in range(rand_index):  # run whats below rand_index number of times
                    current = current.next  # go to the next node till we're at the rand_index number
                    index_counter += 1# update the index counter
                new_node.next = current  # point the new node to the current node
                new_node.prev = current.prev  # point the new node prev to the node that the current node prev is pointing to
                if current.prev:  # link previous node to new node
                    current.prev.next = new_node 
                current.prev = new_node  # assign the current node prev to the new node we just inserted
                if rand_index == 0:  # special case if the new node becomes the head
                    self.head = new_node # assign the new node as the head
                return data, index_counter, f"We have inserted the value {data} at node {index_counter}" # tell us where the new value is inserted.
        self.list_length += 1 # update the length of the linked list


    # Delete ##

    def delete(self, beg = False, rand = False, end = False):
        from random import randint as rdunif # random integer from a discrete uniform distribution
        if beg: #if we are deleting the head of the linked list, if beg == true
            if self.head: # if there exists a head node (it will if the list is not empty)
                self.head = self.head.next # assign the second node to be the head node
                if self.head: # if the head wasn't the only element in the linked list
                    self.head.prev = None # delete the prev pointer from the node we just assigned as the head
                self.list_length -= 1 # update the length of the linked list 
        elif end: # if we are deleting the end of the linked list (tail)
            if self.tail: # does a tail exist on this linekd list (it will if it is not empty)
                self.tail = self.tail.prev # set the tail as the node the tail was previously linked to
                if self.tail: # if the tail wasn't the only elemment in the linked list
                    self.tail.next = None #unlink the previous node from the old tail
                self.list_length -= 1 # update the length of the list
        elif rand:
            rand_index = rdunif(0, self.list_length-1)  # select a random index
            current = self.head  # start at the beginning of the linked list
            index_counter = 0 #so we know which index we deleted the data from
            for _ in range(rand_index): #do whats below rand_index # of times
                current = current.next # traverse the linked list (go to the next Node) to the index we are deleting from
                node_data = current.data # storing the data in the node so that we can tell the user what data we deleted
            if current.prev: # if we are not deleting the head, if current.prev \neq None
                current.prev.next = current.next #point the previous node to the next node
            if current.next: # if we are not deleting the tail, if current.next \neq None
                current.next.prev = current.prev # link the next node to the previous node
            self.list_length-=1 #update the length of the list
            print(f"We have deleted node {rand_index+1} which contained the value {node_data}") # tell the user where and what data was deleted.

    # Linear Search ##
    def search(self, value):
        current = self.head #start at the beginning of the list
        node_counter = 0 # Counter to keep track of the node that we are at, starting at the head (node 0)
        while current: #traverse the list, while current != None
            if value == current.data: #check if the data in the node is the value we are looking for
                    return True, node_counter, f"{value} was found at Node {node_counter}" #if we find it print its location
            else: # if we didn't find it
                current = current.next #go to the next node
                node_counter += 1 #update the index
        return False,f"Item Not found. This took {node_counter} searches." # cannot find the item, inform the user

    # Insertion sort ##
    def sort(self, asc = True, desc = False):
        
        #checking if the linked list is empty or contains one element, itd be already sorted then
        if self.head is None or self.head.next is None: 
            return print("Linked Lists containing 0 or 1 nodes are assumed to be sorted")
        
         # Type check: Ensure all elements are integers, I ASKED CHATGPT TO GIVE ME THIS part. Comments are my own
        current = self.head # start at the head
        while current: # traverse the list
            if not isinstance(current.data, int): # if the data in the node is not an integer
                raise TypeError("All nodes must contain integers to perform sorting") # throw an error and tell the user that all nodes must contain int data
            current = current.next # if the data in the node is an int go the the next
            
        
        # assume that the head is already sorted into its correct position
        current = self.head.next # start at the second node
        while current: # traverse the list, while current \neq None
            x_i_node = current # The node we are comparing against
            x_i_data = current.data # the data in the node we are comparing against
            if desc: #sort in descending order, if desc == True
                while x_i_node.prev and x_i_node.prev.data < x_i_data: # traverse the sorted nodes backwards until we reach the correct position of node x_i
                    x_i_node.prev.data, x_i_node.data = x_i_node.data, x_i_node.prev.data # swap the data of the nodes
                    x_i_node = x_i_node.prev # go the the next node, backwards 
            else: #sort in ascening order, default
                while x_i_node.prev and x_i_node.prev.data > x_i_data: # traverse the sorted nodes backwards until we reach the correct position of node x_i
                    x_i_node.prev.data, x_i_node.data = x_i_node.data, x_i_node.prev.data # swap the data of the nodes
                    x_i_node = x_i_node.prev # go the the next node, backwards 
            current = current.next # go to the next node and compare it with the rest of the sorted nodes
    
    # Printing methods, ChatGPT was my friend for this one. identical to Single linked list, except for <-> instead of -> 
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