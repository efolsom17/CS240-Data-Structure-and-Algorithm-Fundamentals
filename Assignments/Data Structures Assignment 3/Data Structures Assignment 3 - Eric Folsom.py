## Data Structures Assignment 3 - Eric Folsom ##

'''
Implementing a hash table in python. Think that I need to do two different implementations of a hash table
which should be on the different ways to handle collisinos. Want to do a version which implements chaining
and another which implements linear probing. Chaining seems to be the easiest method to start with, deciding on either a linked list or an array.
'''

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [] * size
        
        
    def HashFunc(string, base = int, mod = int):
        hash = 0 # start at 0
        for char in string: # for each character in the string
            hash = ((hash * base) + ord(char)) % mod # compute the hash value for character, stops when we are at the last value
        return hash # return the index for the hash table
    