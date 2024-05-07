## Data Structures Assignment 3 - Eric Folsom ##

'''
Implementing a hash table in python. Think that I need to do two different implementations of a hash table
which should be on the different ways to handle collisinos. Want to do a version which implements chaining
and another which implements linear probing. Chaining seems to be the easiest method. Going to use a linked list.
'''

# double linked list from cs240functions
from cs240functions import DoubleLinkedList as DoubleLinkedList


#Hash table (using Horner's Method for Hashing)
class HashTable:
    
    #Initializing hash table
    def __init__(self, size):
        self.size = size # set the size to be the user defined size
        self.table = [] * size #build an empty hash table of the user defined size.
        
    # function to get a prime number to use with our modulo in the hashing, want to be based on the size 
    # of the hash table, to resolve collisions
    
        
    # Function for hashing values, built in algorithms assignment 5. (slightly modified so I can modify the mod size)     
    def HashFunc(string): 
        base = 31 #going to use 31 for base as I have seen it other places when I looked up what horner's method is
        mod = None# I think I want mod to be dependent on the size of the table.
        hash = 0 # start at 0
        for char in string: # for each character in the string
            hash = ((hash * base) + ord(char)) % mod # compute the hash value for character, stops when we are at the last value
        return hash # return the index for the hash table





## Hash table using some other method for hashing
'''
class HashTable:
    pass
'''