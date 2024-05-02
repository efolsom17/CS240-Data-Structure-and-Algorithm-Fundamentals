### Spring 2024 CS240 Algorithms Assignment 5 - Eric Folsom ###

'''
Creating a hash function using horner's method to hash a string key using unicode code.

base and mod are parameters


horner's method: Take a polynomial and reduce it into a series of multiplications and then sums

((((a_n*x+a_[n-1])x+a_[n-2])x+...)x +a_0, where x is the base.
We then can apply modulus function to the sum at each step, mod n where n is a prime number, makes stuff more uniform
something like:
hash( for a given character in a string) = (hash*(base)+ unicode character value) mod n, hash starts at 0
'''

def HashFunc(string, base = int, mod = int):
    hash = 0 # start at 0
    for char in string: # for each character in the string
        hash = ((hash * base) + ord(char)) % mod # compute the hash value for character, stops when we are at the last value
    return hash # return the index for the hash table

'''

If we were to pass in the string "Whatcom" with a base of say 32 and a mod of say 27, here is how our function would look:
hash = 0 <- this is the starting point

The characters in "Whatcom" are "W","h","a","t","c","o","m", with corresponding unicode (maybe ASCII, im just using ord() to get the value) values:
87, 104, 97, 116, 99, 111, 109

So for each charcter in Whatcom we will compute the following:

hash = ((hash * base) + value) mod n, where base and n are 32 and 27 respectively, thus
hash = ((hash *32)+value) mod 27

So to compute the hash value for the string "Whatcom", we would do as follows:

hash = 0
"W" hash = ((0 * 32) + 87) mod 27 = 6
"h" hash = ((6 * 32) + 104) mod 27 = 26
"a" hash = ((26 * 32) + 97) mod 27 = 11
"t" hash = ((11 * 32) + 116) mod 27 = 9
"c" hash = ((9 * 32) + 99) mod 27 = 9
"o" hash = ((9 * 32) + 111) mod 27 = 21
"m" hash = ((21 * 32) + 109) mod 27 = 25

Thus our hash index for the string "whatcom" is 25 with the specified base and modulus

If we were to apply this function to the strings "Community" and "College" we would get 13 and 19 respectively.
'''