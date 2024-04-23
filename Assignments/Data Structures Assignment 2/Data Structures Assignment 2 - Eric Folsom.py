################ Data Structures Assignment 2 - Eric Folsom ###############
'''
For this assignment I used programiz, w3schools, Grokking, and the Youtube videos on canvas
as resources. They were very helpful, I took a lot of inspiration from the w3schools implementations.
'''


# loading modules
 #importing my linked list structure from data structures assignment 1
from cs240functions import DoubleLinkedList as DoubleLinkedList 
from random import sample as sample

'''
                ###  Stack  ###
                
    Stack is Last in First Out (LIFO)
    
    Implementing a stack in python using an array.
    
    Needs to include the following functions:
        Push
            - Add an element at the largest possible empty array index, i.e the end of the array
        Pop
            - Remove and display the value of the top of the stack
        IsEmpty
            - Check if the size of the stack is 0
        IsFull
            - Check if the size of the stack is full?
                Gonna have to look this up.
        Peek
            - Read the top of the stack
'''

class Stack:
    # Initializing the stack, size is how big you want the stack to be, hope to find a way to make an unspecified size stack, maybe this does this for me, we'll see
    def __init__(self, size = int):
        self.stack = [] # initializing the stack as an array
        self.size_limit = size # setting the "size limit" of the stack
        self.size = len(self.stack)
    
    # push
    def push(self, item): # item is whatever you want to put onto the stack.
        if self.IsFull(): # if we can no longer fit items in the stack
            return print("Stack is full")
        else:
            self.stack.append(item) # appends the stack array
            self.size += 1 # update the size of the stack
    
    # pop
    def pop(self): # read and remove the top item of the stack
        if self.IsEmpty(): # Check if the Stack is empty
            return print("Stack is empty")
        # If the stack contains items
        self.size -= 1
        return self.stack.pop() # Because we are using an array to implement our stack, we can use python's built in pop function on arrays.
    
    # IsEmpty
    def IsEmpty(self): # is the stack empty
        return len(self.stack) == 0 # IsEmpty is True if len(self.stack) is 0
    
    # IsFull
    def IsFull(self): # is the stack full
        return len(self.stack) == self.size_limit # IsFull is True if len(self.stack) equals the specified size limit
    
    # Peek 
    def peek(self): # take a peek a the end of the stack
        if self.IsEmpty(): # if the stack is empty
            return print("Stack is empty") # tell us
        return self.stack[-1] # read the last index in the stack array.


'''
                ### Queue  ###
    
    Queue is First in First out (FIFO)
    
    Impelementing a queue in python using a double linked list.
    
    Need to include the following functions:
        Enqueue
        - adds an item to the back of the queue
        Dequeue
        - reads and removes an item from the front of the queue
        IsEmpty
        - checks if the queue is empty
        IsFull
        - checks if the queue is full
        Peek
        - read the front of the queue
'''

class Queue:
    
    #initializing class
    def __init__(self, size = int):
        temp = [] # my double linked list implementation only takes lists as inputs, empty list
        self.queue = DoubleLinkedList(temp)
        self.size = self.queue.list_length
        self.size_limit = size
    
    # Enqueue
    def enqueue(self, item):
        if self.IsFull():
            return print("The Queue is full.")
        self.size += 1
        return self.queue.insert(item, end = True) # inserts an item at the end of the double linked list that is our queue
        
    
    # Dequeue
    def dequeue(self):
        if self.IsEmpty():
            return print("The Queue is empty")
        self.size -= 1
        value = self.queue.head.data
        self.queue.delete(beg = True)
        return value
    
    # IsEmpty
    def IsEmpty(self):
        return self.size == 0

    # IsFull
    def IsFull(self):
        return self.size_limit == self.size
    
    # Peek
    def peek(self):
        if self.IsEmpty():
            return print("The Queue is Empty")
        return self.queue.head.data
