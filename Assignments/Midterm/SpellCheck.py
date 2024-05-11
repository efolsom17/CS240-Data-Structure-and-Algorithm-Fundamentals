## Spell checker program, CLI and stores the dictionary as a hash table. 
from cs240functions import HashTable
from cs240functions import DoubleLinkedList
from cs240functions import QuickSort
from heapq import nsmallest
import cmd

'''
Accomplishes the following:

1. Load a dictionary of words from a file into the hash table. 

2. Take a string of text as input and check each word in the text against the words in the dictionary stored in the hash table. Your program should identify any words that are not found in the dictionary and display them as "misspelled".

3. Implement a suggestion feature that suggests possible correct spellings for the misspelled words based on edit distance.

4. Implement a Levenshtein distance algorithm to compute the edit distance between two words.

5. Allow the user to add new words to the dictionary and update the hash table accordingly.

6. Handle collisions in the hash table using separate chaining.

7. Optimize the performance of your program in terms of time and space complexity.

8. Your program should be user-friendly and have a command-line interface.

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
            


if __name__ == '__main__':
    SpellCheck().cmdloop()
    