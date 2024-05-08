from cs240functions import DoubleLinkedList as DoubleLinkedList 
class Queue:
    
    #initializing class
    def __init__(self, size = int):
        temp = [] # my double linked list implementation only takes lists as inputs, empty list
        self.queue = DoubleLinkedList(temp) #initialize a doubly linked list
        self.size = self.queue.list_length # set the size of the queue to be the length of the linked list
        self.size_limit = size # set the size limit of th queue, can leave blank if you want none
    
    # Enqueue
    def enqueue(self, item): # add item to the queue
        if self.IsFull(): # check if the queue is full
            return print("The Queue is full.") # tell us
        self.size += 1# increse the size of the list if not full
        return self.queue.insert(item, end = True) # inserts an item at the end of the double linked list that is our queue
        
    
    # Dequeue
    def dequeue(self): # remove and read the front of the queue
        if self.IsEmpty(): # if the queue is empty
            return print("The Queue is empty") # tell us
        self.size -= 1 # decrease the size of the queue
        value = self.queue.head.data # store the value of front of the queue
        self.queue.delete(beg = True) # remove the front of the queue (head of the linked list)
        return value # display the value removed
    
    # IsEmpty
    def IsEmpty(self): # check if the size of the queue is 0
        return self.size == 0

    # IsFull
    def IsFull(self): # check if the size of the queue is the same as the size limit we specified
        return self.size_limit == self.size
    
    # Peek
    def peek(self): # insepect the front of the queue
        if self.IsEmpty(): # if the queue is empty
            return print("The Queue is Empty") # tell us
        return self.queue.head.data # print the value of the head of the queue (do not remove this time).