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

# Some stuff I did while testing:
test1 = stack()
test2 = stack()
test3 = stack()

n = 1

for i in range(n,0,-1):
    test1.push(i)
    
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
        tower_of_hanoi(n-1, starting_rod, ending_rod, middle_rod) # recursive call to move the n-1 disks to the middle rod using the ending rod as the axullary rod
        print(f"Disk {n}: {starting_rod} -> {ending_rod}") # move the current disk
        tower_of_hanoi(n-1, middle_rod, starting_rod, ending_rod) # move the remaining n-1 disks to the ending rod using the starting rod as the auxillary rod
        
### Gonna modify above to work with my idea of using stacks to display the rods and disks.
# Need some funciton to move the top of a stack to the top of another stack
# Something like:
# moveStacks(stack1, stack2):
#   temp = stack1.pop() # pop off the top value of stack1, store it as temp
#   stack2.push(temp) # put the value into stack 2

# function to move the top value of stack 1 to the top of stack 2
def moveStack(stack1 = stack(), stack2 = stack()):
    temp = stack1.pop()
    stack2.push(temp)
    

## Okay after consulting chatgpt about this I need to have a function that creates the stacks then a modified version that works with the function I just wrote:

# tower of of hanoi recursive solution that works on the stacks 
def tower_of_hanoi_stacks(n, starting_rod, middle_rod, ending_rod): # specify the starting rods you want
    if n == 1: # Base case
        moveStack(starting_rod, ending_rod)
        print(f"AFTER\nStarting Rod:\n{starting_rod}\nAuxilary Rod:\n{middle_rod}\nEnding Rod:\n{ending_rod}\
        \n Moved disk {n}")
    else: # if we are not on the last rod
        tower_of_hanoi_stacks(n-1, starting_rod, ending_rod, middle_rod) # recursive call to move the n-1 disks to the middle rod using the ending rod as the axullary rod
        moveStack(starting_rod, ending_rod) # move the current disk
        print(f"AFTER\nStarting Rod:\n{starting_rod}\nAuxilary Rod:\n{middle_rod}\nEnding Rod:\n{ending_rod}\
        \n Moved disk {n}")
        tower_of_hanoi_stacks(n-1, middle_rod, starting_rod, ending_rod) # move the remaining n-1 disks to the ending rod using the starting rod as the auxillary rod


# going to need to call the above:

def TowerOfHanoi(n):# Tower of Hanoi with stacks and it will initialize the number of disks
    # n = number of disks
    
    ## initialize the starting, auxillary, and ending rods
    
    starting_rod = stack()
    auxillary_rod = stack()
    ending_rod = stack()
    
    # fill the starting rod
    for i in range(n,0,-1):
        starting_rod.push(i)
    
    # display starting state
    print("Start:")
    print(f"Starting Rod:\n{starting_rod}\nAuxillary Rod:\n{auxillary_rod}\nEnding Rod:\n{ending_rod}")
    
    # now we can call the tower of hanoi function. It will print its final state
    
    tower_of_hanoi_stacks(n, starting_rod, auxillary_rod, ending_rod)
    


'''
1 mod 3 = 1
2 mod 3 = 2
3 mod 3 = 0
4 mod 3 = 1
5 mod 3 = 2
6 mod 3 = 0
7 mod 3 = 1
'''

# Tower of hanoi iterative

'''
P-code:

going to need to modify my stackMove function to compare the values of things at the top of stacks ( i can bring back moveDisk)

function hanoitoweriterative(n,starting rod, auxillary rod, end rod):
    create stacks for each rod
    fill in the first rod with values 1 through n, with n on the bottom
    add some labels for the rods s,a,e = (Start, Auxilary, End)

    if number of disks are even:
        swap the end pole and the auxilary pole

    for i in range (1, 2**n -1): # itll take 2^n -1 steps to solve the problem, iterate over this range.
        EQUIVALENCY CLASSES WE DEFINED
        if (i % 3 == 1): 
            check even/odd of disk
            if value of disk % 2 ! = 0 
            move between start and end rod, going left (auxillary if n is even,  direction opposite)
            else:
            go in the other direction between the same rods as you just did
            
            actually it would be better to compare the size (value ) of the discs that are on the rods that we are trying to move disks
            to and from. This will determine what move we can make. 

        elif (i % 3 == 2):
            check even/odd of disk
            if value of disk % 2 ! = 0 
            move between start and auxillary rod, going left (end if n is even, direction opposite)
            else:
            go in the other direction between the same rods as you just did

        elif (i % 3 == 0):
            check even/odd of disk
            if value of disk % 2 ! = 0 
            move between auxillary and end rod, going left (if n is even,  direction opposite)
            else:
            go in the other direction between the same rods as you just did
'''

## The grand return of moveDisk!!!!1
## moves a disk between two poles based on the rules of hanoi's tower. It will look at the values of the top disks of the rods that
## we are trying to move disks between and based on the values determine what valid move we can make (direction). 

def moveDisk(start, end, s , e): # start and end are both stacks, s and e are labels for the stacks
    # get the top value of each stack
    topstart = start.pop() 
    topend = end.pop()
    
    # compare values to determine valid movements
    
    # if start is empty
    if topstart == None: # if start rod is empty
        start.push(topend) # move the disk on the end rod to the start rod (only valid move)
        print(f"Disk {topend}: {e} -> {s}") # display the move
    
    # if end is empty
    elif topend == None: # if the end rod is empty
        end.push(topstart) # move disk on start rod to end rod (only valid move)
        print(f"Disk {topstart}: {s} -> {e}") # dispaly the move
        
    # compare the values and move them accordingly, 
    elif topstart > topend: # disk on top of starting rod is bigger than disk on ending rod
        # move disk on end rod to start rod ( only valid move between the two rods)
        start.push(topstart) # put the top value of start back onto the rod
        start.push(topend) # put the top value of end on top of the start rod
        print(f"Disk {topend}: {e} -> {s}") # display the move
    else: #disk on top of starting rod is smaller than the disk on the ending rod
        # move the disk on the start rod to the end rod ( only valid move between the two rods)
        end.push(topend) # put the top value of end back onto the end rod
        end.push(topstart) # put the top value of start on top of the end rod
        print(f"Disk {topstart}: {s} -> {e}") # display the move

def tower_of_hanoi_it(n, start, aux, end):
    # initialize stacks
    start = stack(n)
    aux = stack(n)
    end = stack(n)
 
    
    # fill in starting stack (rod)
    for i in range(n,0,-1):
        start.push(i)
    
    #labels for printing
    s, a, e = 'Start', 'Aux', 'End'
    
    # check if n is even or odd, have to change some things if that is the case
    if (n % 2 == 0):
        # swap auxilary and end rods, the first step that will be made ( so we are moving disks between the correct rods)
        temp = e 
        e = a
        a = temp
    
    
    
    #iterate through the number of moves
    for i in range(1,int(2**n)): # range 1 to 2^n-1, but because of how python's range function works we can just write 2^n
        if (i % 3 == 1): # valid move between start and end rod (start and auxillary if n is even)
            moveDisk(start, end, s, e) # function to move the rods
        elif (i % 3 == 2): # valid move between start and auxillary rod (start and end if n is even)
            moveDisk(start, aux, s, a) # function to move the rods
    
        elif (i % 3 == 0): # valid move between auxillary and end rod
            moveDisk(aux, end, a, e) # funciton to move the rods
        

# Tower of Hanoi more than 3 pegs, but only 3 disks

def THanoiG3R(n): # number of rods, done with three disks.
    
    if n <3:
        return f"Puzzle must have at least 3 pegs"
    if n == 3:
        return tower_of_hanoi(3, "Start", "Auxillary", "End")
    if n > 3:
        nopen = n -1 
        auxopen = nopen-1
        print(f"Disk 1: Start -> Auxillary ({auxopen} available)")
        auxopen -= 1
        print(f"Disk 2: Start -> Auxillary ({auxopen} available)")
        print(f"Disk 3: Start -> End")
        print(f"Disk 2: Auxillary -> End")
        print(f"Disk 1: Auxillary -> End")

    
'''
Tower of Hanoi Resources:

https://www.youtube.com/watch?v=PGuRmqpr6Oo
https://www.youtube.com/watch?v=2SUvWfNJSsM # inspiration for iterative version also helped me wrap my head around the recursion going on as well.
https://www.youtube.com/watch?v=bdMfjfT0lKk
https://www.geeksforgeeks.org/iterative-tower-of-hanoi/
https://en.wikipedia.org/wiki/Tower_of_Hanoi#Frame%E2%80%93Stewart_algorithm
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
https://medium.com/@ethannam/understanding-the-levenshtein-distance-equation-for-beginners-c4285a5604f0 # super helpful to get me thinking about matrices again.
https://en.wikipedia.org/wiki/Wagner%E2%80%93Fischer_algorithm 
https://en.wikipedia.org/wiki/Levenshtein_distance
https://www.youtube.com/watch?v=XYi2-LPrwm4 this video went over my head when I watched it, but I just decided to watch/read as much as possible and kind of brute force the understanding
https://www.youtube.com/watch?v=d-Eq6x1yssU&t Really good explanation of the wagner fischer algorithm to compute the levenshtein edit distance


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


### Wagner Fischer Algorithm for levenshtein distance
def levDist(str1, str2):
    m = len(str1)
    n = len(str2)
    # initialize distance matrix
    distance = [[0 for j in range(n+1)] for i in range(m+1)]
    # i, row
    # j, column
    # distance[i][j], value at row i, column j
    
    distance[0][0] = 0 # comparing two empty strings, 0 comparisons to start
    
    # fill in the first row (comparing any prefix of str2 to an empty str1)
    for j in range(1,n+1):
        distance[0][j] = j

    # fill in the first column (comparing any prefix of str1 to an empty str2)
    for i in range(1,m+1):
        distance[i][0] = i
    
    # compare strings follow the same rules as recursion
    # comparing at row, column pair distance(i,j)
    
    # for each row
    for i in range(1,m+1): # row 0 is the empty string row
        # go to colum j so we can compare prefixes at the row,column pair i,j in the respective strings
        for j in range(1,n+1): # column 0 is the empty string column
            
            # calculate the substitution cost, 1 if the characters match, 0 if we don't have to change anything
            if str1[i-1] == str2[j-1]: # characters match
                sub = 0 # no substitution cost
            else: # characters don't match
                sub = 1 # substitution cost of 1
            # insert edit cost at distance[i][j] based on the costs set during the recursive version
            # calculates minimum edit distance for the pair i,j
            distance[i][j] = min(
                distance[i][j-1]+ 1, # insert a character, add 1 because we are making an edit
                distance[i-1][j]+ 1, # delete a character, add 1 because we are making an edit
                distance[i-1][j-1] + sub # substitute or don't change the character
            )
    return distance[m][n]

# This works now, kind of returns a slightly different matrix than what I had imagined it would be, but this is basically my quick and dirty implementation of it based on what I read about the algorithm
    
    
def misspelled(string):
        temp = string.split()# split the string into each word, store it as a temp variable
        spellings = []# created an empty array the length of the temp variable ( call it spellings)
        for word in temp:# for each word in the temp variable:
         #   run dictionary.contains(word) and append the spellings array with the truth value
            spellings.append(not(dictionary.contains(word)))
        # return the spellings array
        return spellings
    
def do_check(string):
    'Check the spelling of a string'
    if not string: # ensure that a string has been passed through
        print("You must enter a string") # tell the user to enter a string
        return
    print(f"Input: {string}")
    spellings = misspelled(string) # returning just the string doesn't work, because if anything is true it exits the CLI loop.
    string_words = string.split()
    string_misspell = []
    for i in range(0,len(spellings)-1):
        string_misspell.append((string_words[i],spellings[i]))
    for word, misspell in string_misspell:
        if misspell:
            print(f"{word} is spelled wrong") # tell the user the word is misspelled
            suggestions = suggest(word) # get the suggestions for the word
            print("Suggested replacements:") # print the suggested replacement words.
            for item in suggestions:
                print(item)
    return
  
'''

Okay how do I create a CLI program?????

using the cmd module because it seems like its the friendliest to work with.
'''


class SpellCheck(cmd.Cmd):
    intro = "~~~~~~~~~~~ Spell Check Program ~~~~~~~~~~~\
        \n Check the spelling of a string using 'check string'\
        \n Add a new word to the dictionary with 'add word'\
        \n View the dictionary with 'dictionary'\
        \n Exit with 'exit'"
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
    
    
    def suggest(self, string):
        edit_distance = [] # store the edit distance
        dictionary = self.dictionary
        for index in dictionary.table: # for each index in the hash table
            if index.head: #check if empty 
                current = index.head # start at the head of the linked list for that index
                while current: # traverse the list
                    editdist = self.levenshteinDist(string, current.data) # calculate the edit distance using levenshtein distance
                    edit_distance.append((editdist, current.data))
                    current = current.next
    
        min5 = nsmallest(5, edit_distance, key = lambda x: x[0]) #get the 5 words with the smallest edit distance, stored as a tuple (edit distance, key)
    
         # get just the keys from the min5 list and "suggest" them, kinda cheating with this, going to make changes.
        suggestions =  [key for _, key in min5]
        return suggestions


    def levenshteinDist(self, str1, str2):
        m = len(str1)
        n = len(str2)
        # initialize distance matrix
        distance = [[0 for j in range(n+1)] for i in range(m+1)]
        # i, row
        # j, column
        # distance[i][j], value at row i, column j
        
        distance[0][0] = 0 # comparing two empty strings, 0 comparisons to start
        
        # fill in the first row (comparing any prefix of str2 to an empty str1)
        for j in range(1,n+1):
            distance[0][j] = j

        # fill in the first column (comparing any prefix of str1 to an empty str2)
        for i in range(1,m+1):
            distance[i][0] = i
        
        # compare strings follow the same rules as recursion
        # comparing at row, column pair distance(i,j)
        
        # for each row
        for i in range(1,m+1): # row 0 is the empty string row
            # go to colum j so we can compare prefixes at the row,column pair i,j in the respective strings
            for j in range(1,n+1): # column 0 is the empty string column
                
                # calculate the substitution cost, 1 if the characters match, 0 if we don't have to change anything
                if str1[i-1] == str2[j-1]: # characters match
                    sub = 0 # no substitution cost
                else: # characters don't match
                    sub = 1 # substitution cost of 1
                # insert edit cost at distance[i][j] based on the costs set during the recursive version
                # calculates minimum edit distance for the pair i,j
                distance[i][j] = min(
                    distance[i][j-1]+ 1, # insert a character, add 1 because we are making an edit
                    distance[i-1][j]+ 1, # delete a character, add 1 because we are making an edit
                    distance[i-1][j-1] + sub # substitute or don't change the character
                )
        return distance[m][n]
        
        
    
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
        string_words = string.split()
        string_misspell = []
        for i in range(0,len(spellings)-1):
            string_misspell.append((string_words[i],spellings[i]))
        for word, misspelled in string_misspell:
            if misspelled:
                print(f"{word} is spelled wrong") # tell the user the word is misspelled
                suggestions = self.suggest(word) # get the suggestions for the word
                print("Suggested replacements:") # print the suggested replacement words.
                for item in suggestions:
                    print(item)
        return
            
                
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