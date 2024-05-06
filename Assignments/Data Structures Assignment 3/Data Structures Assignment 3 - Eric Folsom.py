## Hashing function 

def HashFunc(string, base = int, mod = int):
    hash = 0 # start at 0
    for char in string: # for each character in the string
        hash = ((hash * base) + ord(char)) % mod # compute the hash value for character, stops when we are at the last value
    return hash # return the index for the hash table


class HashTable:
    pass