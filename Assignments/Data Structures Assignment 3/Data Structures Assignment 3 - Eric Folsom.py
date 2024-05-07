## Data Structures Assignment 3 - Eric Folsom ##

'''
Implementing a hash table in python. Think that I need to do two different implementations of a hash table
which should be on the different ways to handle collisinos. Want to do a version which implements chaining
and another which implements linear probing. Chaining seems to be the easiest method. Going to use a linked list.
Going to be very basic and not inserting a key, data pair only inserting a key into the hash table,
'''

# double linked list from cs240functions
from cs240functions import DoubleLinkedList as DoubleLinkedList


#Hash table (using Horner's Method for Hashing)
class HashTable:
    
    #Initializing hash table
    def __init__(self, size):
        self.size = size # set the size to be the user defined size
        self.table = [] * size #build an empty hash table of the user defined size.
        
    # functions to get a prime number to use with our modulo in the hashing, want to be based on the size 
    # of the hash table, should in theory limit collisions
    # I got this code and the idea to implement something like this from programiz 
    
    def isPrime(n): # Checking if a number is prime (has more than itself and 1 as its divisors and is greater than 1)
        if n == 1 or n == 0: # if the number is 1 or 0
            return False # not a prime, must be greater than 1
        for i in range(2, n//2): # Checks if the number is divisble by every number up to n/2, any more than that is pointless
            if n % i == 0: # if the remainder is 0, i.e, n is divisble by i
                return False # the number is not a prime
        # if we make it all the way through and the above has not been satisfied
        return True # then the number is prime

    # This function gets the prime number closest to the size of the hash table.
    def getPrime(n): # Assumed that n is the size of the hash table so we will work downwards
        if n % 2 == 0: # Check if n is even ( even numbers are not prime)
            n = n - 1 # ensure that n is odd
        while not isPrime(n): # call the isPrime function above to check if the number is prime, while this is not true
            n -=2 # go to the next odd number, 
        # once isPrime(n) == True
        return n # return the prime number
        

    
        
    # Function for hashing values, built in algorithms assignment 5. (slightly modified so I can modify the mod size)     
    def HashFunction(string): 
        base = 31 #going to use 31 for base as I have seen it other places when I looked up what horner's method is
        mod = getPrime(self.size)# I think I want mod to be dependent on the size of the table. Mod using above two helper functions
        hash = 0 # start at 0
        for char in string: # for each character in the string
            hash = ((hash * base) + ord(char)) % mod # compute the hash value for character, stops when we are at the last value
        return hash # return the index for the hash table





## Hash table (using some other method for hashing)
'''
class HashTable:
    pass
'''