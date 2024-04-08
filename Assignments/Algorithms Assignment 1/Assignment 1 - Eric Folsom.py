######Eric Folsom - Algorithms Assignment 1 - CS240 Spring 2024 #######################################
#################### Setup Chunk loading the required libraries     ###################################
import numpy as np
import pandas as pd

#######################
## Problem 2 #####

def binary_search(item, data, oper = False, diag = False):

   # item: item in the data that we are interested in finding
   # data: list or array of data with items we are interested in finding, assumes
   # integer data
   # oper: Logical T or F. Choose weather to include the number of operations. 
   #        Default: False.
   # diag: T or F. Choose to see the inner workings of the algorithm.
   #        Default: False.

   # Begin by defining some variables for keeping track of x0 and xn
   # as well as keeping track of the number of operations

   x0 = 0 #defining the index of first element of the array
   xn = len(data)-1 #defining the index of the last element of the array
   operations = 0 #creating a varaible to count the number of operations the 

   # Beginning the actual function
   while x0 <= xn: #while we are searching valid indicies of our array
      operations = operations + 1 #count one operation
      mid = (xn + x0) // 2 #pick the middle index of the array (floor operation)
      search = data[mid] # Value of the middle index (the one we are searching in)

      #Diagnostics/Inner workings
      #I had to use this a few times
      if diag == True:
        print('Lowest Index: ', 
         x0,"\nHigh Index: ",xn,
         "\nIndex we are searching is: ",mid,
          " Value: ",search) 
      
      #if the item we are searching for is the same as the value of the array
      if search == item: 
         #if you want to see the number of operations
         if oper == True: 
            #return the index of the item and the number of
            #  operations it took to find the item
            return print("Item ",
             item,
             ' is located at index',
              mid,
               ".\n This took ",
                operations,
                ' operations.') 
         else:
            #return the position of the item
            return print("Item ", item,' is located at index', mid) 

      # if our guess is too low
      elif search < item:
          #update the low index position to be the middle guess. 
          # Adding 1 so we don't recheck the same index twice
         x0 = mid + 1
         #diagnostics
         if diag == True:
           print('Search was too low') #debugging

      # if our guess is too high
      elif search > item: 
         # update the high position to be the middle guess. 
         # Subtracting 1 so we don't check the same index
         # twice, as that would be slow.
         xn = mid - 1 
         #diagnostics:
         if diag == True:
            print("Search was too high") #debugging

   # if we can't find the item in the array.
   return print("Item Not Found\nThis took ", operations, ' operations.') 


########################################################################################################
########################################################################################################

### Problem 3 Code #####

## Importing the numbers data using the Pandas library

numbers = pd.read_csv("C:\\Users\\ericf\\OneDrive\\Desktop\\WCC\\CS240 Data Structure and Algorithm Fundamentals\\Assignments\\Algorithms Assignment 1\\Data\\numbers.txt",
header=None,
sep='\t'
) #importing the numbers data as a data frame

## Converting Numbers to an array using Numpy##
numbers = numbers.to_numpy()
#now back to base python for ease of use with the algorithm I just wrote:
numbers = numbers.tolist()
#fixing some jankiness with importing the data so that all the elements of the list are integers instead of being lists of length 1, thanks ChatGPT.
con_numbers = [num[0] for num in numbers]
numbers = con_numbers


#### a.
binary_search(51216352, numbers, oper=True)

### b.
binary_search(198313119, numbers, oper=True)

### c. 
binary_search(196614208,numbers, oper=True)