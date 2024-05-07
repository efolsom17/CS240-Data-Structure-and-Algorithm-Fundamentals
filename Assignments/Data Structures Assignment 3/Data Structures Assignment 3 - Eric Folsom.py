## Data Structures Assignment 3 - Eric Folsom ##

'''
Implementing a hash table in python. Think that I need to do two different implementations of a hash table
which should be on the different ways to handle collisinos. Want to do a version which implements chaining
and another which implements linear probing. Chaining seems to be the easiest method. Going to use an array for chaining.
Going to be very basic, inserting a (key, data) I scrapped a lot of my above ideas, because I ran out of time because of the midterm :/.
'''



#Hash table (using Horner's Method for Hashing) This one inserts a (key, value) pair into the hash table
class HashTable:
    
    #Initializing hash table
    def __init__(self, size):
        self.size = size # set the size to be the user defined size
        self.table = [None] * size #build an empty hash table of the user defined size.
        
    # functions to get a prime number to use with our modulo in the hashing, want to be based on the size 
    # of the hash table, should in theory limit collisions
    # I got this code and the idea to implement something like this from programiz 
    
    def _isPrime(self,n): # Checking if a number is prime (has more than itself and 1 as its divisors and is greater than 1)
        if n == 1 or n == 0: # if the number is 1 or 0
            return False # not a prime, must be greater than 1
        for i in range(2, n//2): # Checks if the number is divisble by every number up to n/2, any more than that is pointless
            if n % i == 0: # if the remainder is 0, i.e, n is divisble by i
                return False # the number is not a prime
        # if we make it all the way through and the above has not been satisfied
        return True # then the number is prime

    # This function gets the prime number closest to the size of the hash table.
    def _getPrime(self,n): # Assumed that n is the size of the hash table so we will work downwards
        if n % 2 == 0: # Check if n is even ( even numbers are not prime)
            n = n - 1 # ensure that n is odd
        while not self._isPrime(n): # call the isPrime function above to check if the number is prime, while this is not true
            n -=2 # go to the next odd number, 
        # once isPrime(n) == True
        return n # return the prime number

        
    # Function for hashing values, built in algorithms assignment 5. (slightly modified so I can modify the mod size)     
    def HashFunction(self, string): 
        base = 31 #going to use 31 for base as I have seen it other places when I looked up what horner's method is
        mod = self._getPrime(self.size)# I think I want mod to be dependent on the size of the table. Mod using above two helper functions
        hash = 0 # start at 0
        for char in string: # for each character in the string
            hash = ((hash * base) + ord(char)) % mod # compute the hash value for character, stops when we are at the last value
        return hash # return the index for the hash table

    # Function to insert values into the hash table (key is assumed to be a string)
    def insert(self, key, value):
        # Get the index that the value associated with the key should be inserted in
        index = self.HashFunction(key)
        # if the index is empty, initialize it as an empty array
        if self.table[index] == None: #checks if it is emtpy
            self.table[index] = [] # initializes it as an array
        # append the key and value to the array at the position, chains the values using arrays if there are collisions
        self.table[index].append((key, value))
    
    # Function to retrieve a value from the hash table given a string,
    def get(self, key):
        # find the index of the key
        index = self.HashFunction(key)
        if self.table[index] != None: # if the hash corresponding to the key contains data
            # go to the key, and then return the corresponding value associated to it
            for k,v in self.table[index]: # for each key,value pair in the index of our hash table
                if k == key: # if we are at the key,
                    return v # return the value associated with it
        # else if the index is empty or there is stuff assigned to the index but they key isn't present
        return print(f"{key} Not Found") # tell us that the key isn't present
    
    # Function to delete a value from the hash table ( replace it with none)
    def delete(self, key):
        #find the index of the key we want
        index = self.HashFunction(key)
        #go to the index and see if it contains data (possible collisions)
        if self.table[index] != None:
            # search the index to see if the key is present
            i = 0 # index in the bucket (index of the big hash table)
            for k,v in self.table[index]:
                if k == key: # if we are at the key
                    del self.table[index][i] # delete the key
                i += 1 # tells us that we went to the next index of the bucket
        if not self.table[index]: #if the bucket (index of the big hash table) is empty 
            # self.table[index] is True if it has items in it, and false if is empty, so if it is empty not self.table[index] is True
            self.table[index] = None # if the bucket is empty mark it as None so that it can be filled later.
        # else if the index is empty or there is stuff assigned to the index but they key isn't present
        return print(f"{key} Not Found") # tell us that the key isn't present
     
    
    # Some way to represent the hash table when we print it or repr it, also might be cool to display it somehow.
    # (ChatGPT was helpful for this)\
    def display(self):
        return self.table
    
    def __repr__(self):
        return f'HashTable(size = {self.size}, table = {self.table})'



## Hash table (using some other method for hashing) also only hashes a string no value attached to it 
# ( I am going to need this on the midterm so I might as well do it now)

class HashTableString:
    #Initializing hash table
    def __init__(self, size):
        self.size = size # set the size to be the user defined size
        self.table = [None] * size #build an empty hash table of the user defined size.
        
    # functions to get a prime number to use with our modulo in the hashing, want to be based on the size 
    # of the hash table, should in theory limit collisions
    # I got this code and the idea to implement something like this from programiz 
    
    def _isPrime(self,n): # Checking if a number is prime (has more than itself and 1 as its divisors and is greater than 1)
        if n == 1 or n == 0: # if the number is 1 or 0
            return False # not a prime, must be greater than 1
        for i in range(2, n//2): # Checks if the number is divisble by every number up to n/2, any more than that is pointless
            if n % i == 0: # if the remainder is 0, i.e, n is divisble by i
                return False # the number is not a prime
        # if we make it all the way through and the above has not been satisfied
        return True # then the number is prime

    # This function gets the prime number closest to the size of the hash table.
    def _getPrime(self,n): # Assumed that n is the size of the hash table so we will work downwards
        if n % 2 == 0: # Check if n is even ( even numbers are not prime)
            n = n - 1 # ensure that n is odd
        while not self._isPrime(n): # call the isPrime function above to check if the number is prime, while this is not true
            n -=2 # go to the next odd number, 
        # once isPrime(n) == True
        return n # return the prime number

        
    # Function for hashing values, Using summation method that I saw on w3schools    
    def HashFunction(self, string): 
        base = 31 #going to use 31 for base as I have seen it other places when I looked up what horner's method is
        mod = self._getPrime(self.size)# I think I want mod to be dependent on the size of the table. Mod using above two helper functions
        sum_char = 0 # starts at 0, sum of the charachters in the string's unicode values
        for char in string: # for each character in the string,
            sum_char += ord(char) # add the unicode value
        hash = sum_char % mod # hash value sum of the unicode characters mod prime number smaller than hash size
        return hash # return the hash value
    
    # function to insert a key into the hash table
    def insert(self, key):
        # get the index of the bucket that the key should go in
        index = self.HashFunction(key)
        # if the bucket does not exist, create it
        if self.table[index] == None:
            self.table[index] = []
        # else (or after we initialize the bucket), add the item to the bucket
        self.table[index].append(key)
    
    # function to check if a key is present in the hash table
    # (I pretty much stole this from w3schools, I was going to do something very similar to what I did
    # for the key, value hash table but this was a lot more elegant, so I went with it)
    def contains(self, key):
        # get the hash that the key should be
        index = self.HashFunction(key) 
        # check if the key is there
        bucket = self.table[index] # bucket is the index we are in
        return key in bucket # returns true if the key is present in the bucket
    
    # funciton to remove a key from the hash table
    def remove(self, key):
        # Go to the index of the key
        index = self.HashFunction(key)
        # check if the bucket contains stuff
        if self.table[index] != None:
        # check if the item is in the bucket
            if key in self.table[index]: # if the key is in the bucket
                self.table[index].remove(key) # remove the key from the bucket
                # removing the bucket if it is now empty
                if not self.table[index]: # if the bucket is empty this will return true and evaluate
                    self.table[index] = None # remove the bucket (set the index equal to None)
                    return True
        return False
    
    # some ways to display the hash table
    def display(self):
        return self.table
    def __repr__(self) -> str:
        return f"HashTableString: Size = {self.size}, table = {self.table}"
 



#testing
  
words = ["The" ,"Quick" ,"Brown" ,"Fox" ,"Jumped", "Over", "the", "Lazy" ,"Dog"]
test = HashTableString(10)
for word in words:
    test.insert(word)

test.display()
test.remove("Dog")
test.insert("Cat")
test.contains("Quick")
test.contains("Slow")
test.display()



