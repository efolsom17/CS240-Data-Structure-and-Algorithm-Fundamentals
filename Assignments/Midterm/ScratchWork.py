## Packages ##
from cs240functions import Stack as stack
from cs240functions import HashTable
from cs240functions import DoubleLinkedList
from cs240functions import QuickSort
from heapq import nsmallest
import cmd


## Tower of Hanoi ##

# Hanoi's Tower implementation in python
# Would Like to use stacks for this implementaion:
# Took some inspiration for implementing this on how I have seen other people implement this algorithm, 
# But would like to modify the implementations to store the states of the tower as separate stacks. 
# To make it clearer, I would like each rod to be its own stack and we will move items in the stack (discs)
# between stacks to demonstrate the actual tower of hanoi problem with physical rods and discs. I will store numbers
# in the stacks which will represent the radius of a disc. So each stack will look like as follows at the beginning if we had 3 discs to move
# [1]   []      []
# [2]   []      []
# [3]   []      []
#
# Which after runnning the algorithm would look like:
# []    []      [1]
# []    []      [2]
# []    []      [3]

from cs240functions import Stack as stack

# Some stuff I did while testing:
test1 = stack()
test2 = stack()
test3 = stack()

n = 1

for i in range(n,0,-1):
    test1.push(i)
    test2.push(None)
    test3.push(None)
    
test4 = [test1,test2,test3]
test4



''''
Hanoi's Tower using Recursion
'''
#getting this working first then going to try to implement this using a stack
def tower_of_hanoi(n, starting_rod, middle_rod, ending_rod): # specify the starting rods you want
    if n == 1: # Base case
        print(f"Disk {n}: {starting_rod} -> {ending_rod}") # Move the specified disk 
    else: # if we are not on the last rod
        tower_of_hanoi(n-1, starting_rod, ending_rod, middle_rod) # recursive call to move the n-1 disks to the middle rod
        print(f"Disk {n}: {starting_rod} -> {ending_rod}") # move the current disk
        tower_of_hanoi(n-1, middle_rod, starting_rod, ending_rod) # 
        
        
### Gonna modify above to work with my idea of using stacks.


'''
Tower of Hanoi Resources:

https://www.youtube.com/watch?v=PGuRmqpr6Oo
https://www.youtube.com/watch?v=2SUvWfNJSsM # inspiration for iterative version also helped me wrap my head around the recursion going on as well.
https://www.youtube.com/watch?v=bdMfjfT0lKk
'''



## Spellchecker ## 



## Spell checker program, needs to be CLI and stores the dictionary as a hash table. 
from cs240functions import HashTable
from cs240functions import DoubleLinkedList
from heapq import nsmallest

'''
Must do the following:

1. Load a dictionary of words from a file into the hash table.  You will need to create this yourself.  Aim for 20 to 100 words. (oops I did 1000 words for my dictionary) 

EaSY

2. Take a string of text as input and check each word in the text against the words in the dictionary stored in the hash table. Your program should identify any words that are not found in the dictionary and display them as "misspelled".

Did this, returns an array with the True if a word is misspelled and False if a word is correctly Spelled.

3. Implement a suggestion feature that suggests possible correct spellings for the misspelled words based on edit distance.

4. Implement a Levenshtein distance algorithm to compute the edit distance between two words.

5. Allow the user to add new words to the dictionary and update the hash table accordingly.

6. Handle collisions in the hash table using separate chaining.

Chains using double linked list to store collisions.

7. Optimize the performance of your program in terms of time and space complexity.

going to implement levenshtein distance recursively first then go and make it iteratively by filling out a matrix, might try my hand at dynamic programing.

8. Your program should be user-friendly and have a command-line interface.

'''


# loading the dictionary, 1000 most common words in the english language and loading it into a hash table.


n = 1000 # hash table size
dictionary = HashTable(n)
with open("./Data/dictionary.txt", "r") as words:
    words = [line.strip() for line in words] 
for word in words:
    dictionary.insert(word)
del words


def getdict(hashtable):
    temp = [] # Initialize an empty list to store the keys
    for index in hashtable.table: # Traverse each index in the hash table
        current = index.head # start at the head of the linked list at the index
        while current: # traverse the list
            temp.append(current.data) # add the keys to the temp array
            current = current.next # go to the next node of the linked list in the hash table
    return temp

    
#  fucntion to take a string of text and check each word in the text against the words in the hash table and identify any "misspellings".

def Misspell(string):
    temp = string.split()# split the string into each word, store it as a temp variable
    spellings = []# created an empty array the length of the temp variable ( call it spellings)
    for word in temp:# for each word in the temp variable:
    #   run dictionary.get(word) and append the spellings array with the truth value
        spellings.append(not(dictionary.contains(word)))
    # return the spellings array
    return spellings

# True indicates that the word is misspelled.

'''
Function to suggest a word to replace misspelled word with using edit distance

def suggest(string):
    edit_distance = [] # store the edit distance
    for index in hashtable (dictionary.table): # for each index in the hash table
        if index.head: check if empty 
            current = index.head # start at the head of the linked list for that index
                while current: # traverse the list
                    editdist = Calculate the edit distance(string, current.data) # calculate the 
                    edit_distance.append((editdist, key))
                    current = current.next
    
    min5 = nsmallest(5, edit_distance, key = lambda x: x[0]) #get the 5 words with the smallest edit distance, stored as a tuple (edit distance, key)
    
    get just the keys from the min5 list and "suggest" them
    suggestions =  [key for _, key in min5]
    return suggestions
    

Okay I have that garbage done with now to figure out levenshtiens distance algorithm. From what I have seen it is a recursive algorithm that can be complex with long strings, but I think the recursive approach should be fine for this problem.

I know that it works by comparing the number of changes that you have to make to make two strings the same. You are allowed to make 3 different operations:
1. Insert a Character
2. Delete a Character
3. Substitute a charachter for another character. (most powerful, technically two operations, will be the optimal solution since you can just substitute)

Calculates the minimum number of edits it would take to make two strings the same string. 

Basing this algorithm based on the peicewise function that I saw on wikipedia (https://en.wikipedia.org/wiki/Levenshtein_distance). I think from here on out I will try to make my pseudocode in that style as it fits my brain a lot better than if I try to write it like I am writing code for now. 


levensteindist(strA, strB):
# start comparing each string from the end because python
    i = len(strA) 
    j = len(strB)
    
    # if one of the strings are empty, base case 
    if i == 0
        return j # it will take j deletions to make both the strings empty
    if j == 0
        return i # it will take i deletions to make both the strings empty
        
    # recursive case 1 characters in both strings match, call the function on the rest of each string, no changes so don't count an edit
    if strA[i-1]==strB[j-1]:
        levensteinhist(strA[i-1],strB[j-1])
    
    # Recursive case 2, characters do not match, now we have to calculate the number of operations. by either inserting a character, deleting a character, or doing a substitution of a character.
    # return the minimum operations doing the following: add 1 each time because we are making an edit.
    
    insert = levenworth(strA, strB[:-1]) # insert the last character form string B into string A so that they have the same character, recursively call the levenshtein algorithm again on string A and the rest of string B add one for the cost of the operation
    delete = levenshtin(strA[:-1], strB) # delete the last character from string A , recursively call the funciton on the rest of string A and all of string B
    substitute = leven(strA[:-1], strB[:-1]) # substitute a character in string A for the character in string B, then recursively call the function on the rest of string A and B
    
    return 1+ min(insert, delete, substitute)

Recursion is going to get really bad when the words are long :/, good thing my dictionary has small words ;)


Levenshtein Resources:



'''
# time to try to implement the above in code:

def suggest(string):
    edit_distance = [] # store the edit distance
    for index in dictionary.table: # for each index in the hash table
        if index.head: #check if empty 
            current = index.head # start at the head of the linked list for that index
            while current: # traverse the list
                editdist = levenshteinDist(string, current.data) # calculate the edit distance using levenshtein distance
                edit_distance.append((editdist, current.data))
                current = current.next
    
    min5 = nsmallest(5, edit_distance, key = lambda x: x[0]) #get the 5 words with the smallest edit distance, stored as a tuple (edit distance, key)
    
    # get just the keys from the min5 list and "suggest" them
    suggestions =  [key for _, key in min5]
    return suggestions


def levenshteinDist(strA, strB):
    i = len(strA) # length of string A
    j = len(strB) # length of string B
    
    ## Check if either of the strings are empty ( base case )
    
    if  i == 0: # string A is empty
        return j # length of string B for number of delete edits needed
    if j == 0: # string B is empty
        return i
    
    ## Recursive case 1, both characters match, compare the rest of both strings
    
    if strA[i-1] == strB[j-1]: # if the last characters of strings A and B are the same
        return levenshteinDist(strA[:-1],strB[:-1]) # recursively call the function on the remaining characters in both strings.
    
    # Recursive case 2, characters don't match, calculate the amount of edits needed to make the strings match:
    return 1 + min( # adds 1 each time any of these are invoked, cost of doing the edit operation
            levenshteinDist(strA, strB[:-1]), # insert character into string A from string B
            levenshteinDist(strA[:-1], strB), # delete the last character from string A
            levenshteinDist(strA[:-1], strB[:-1]) # substitute the last character in string A for the last character in string B.
            )
        
    
'''

Okay how do I create a CLI program?????

using the cmd module because it seems like its the friendliest to work with.
'''


class SpellCheck(cmd.Cmd):
    intro = "~~~~~ Spell Check Program ~~~~~\n Check the spelling of a string using 'spellcheck string' \n Add new word(s) to the dictionary with 'add word(s)'\n View the dictionary with 'dictionary '"
    prompt = ""
    def do_exit(self, arg):
        'Exit the shell'
        print("Exiting")
        return True  # return True to stop the cmd loop
 
    def __init__(self):
        super().__init__()  # Initialize the Cmd superclass
        # loading the dictionary, 1000 most common words in the english language and loading it into a hash table.
        n = 1000 # hash table size
        self.dictionary = HashTable(n)
        with open("./Data/dictionary.txt", "r") as words:
            words = [line.strip() for line in words] 
        for word in words:
            self.dictionary.insert(word)
        
    
    def misspelled(self, string):
        temp = string.split()# split the string into each word, store it as a temp variable
        spellings = []# created an empty array the length of the temp variable ( call it spellings)
        for word in temp:# for each word in the temp variable:
         #   run dictionary.contains(word) and append the spellings array with the truth value
            spellings.append(not(self.dictionary.contains(word)))
        # return the spellings array
        return spellings
    
    def do_check(self, string):
        'Check the spelling of a string'
        if not string: # ensure that a string has been passed through
            print("You must enter a string") # tell the user to enter a string
            return
        print(f"Input: {string}")
        spellings = self.misspelled(string) # returning just the string doesn't work, because if anything is true it exits the CLI loop.
        for word, misspelled in zip(string.split(),spellings):
            if misspelled:
                print(f"{word} is spelled wrong")
                # suggest words fuction goes here
                # print the 5 suggestions
                
    def do_add(self, string):
        'Add a word to the dictionary'
        self.dictionary.insert(string) # hash the string, could be more than one word.
    
    #need a function to get all the items in the dictionary store as an arrray so so I can display it
    def _getdict(self, hashtable):
        temp = [] # Initialize an empty list to store the keys
        for index in hashtable.table: # Traverse each index in the hash table
            current = index.head # start at the head of the linked list at the index
            while current: # traverse the list
                temp.append(current.data) # add the keys to the temp array
                current = current.next # go to the next node of the linked list in the hash table
        return temp
            
    # display the dictionary 
    def do_dictionary(self, x =None):
        dictionary_presentation = self._getdict(self.dictionary) # call the getdict function to store the dictionary
        dictionary_presentation = QuickSort(dictionary_presentation)
        for item in dictionary_presentation:
            print(item)
    
    
    
    
#SpellCheck().cmdloop()