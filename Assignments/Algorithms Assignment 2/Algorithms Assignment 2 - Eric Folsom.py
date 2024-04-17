## Algorithms Assignment 2 - Eric Folsom ##


# for testing purposes, randomizing my testing sample
from random import sample as sample
from random import seed as set_seed

set_seed(12345) # reproducible randomization

# Testing Array

test_numbs = sample(list(range(100)), 100)

## Importing the numbers-1.txt data

with open("./Data/numbers-1.txt", "r") as nums: #opens the file
    numbers1 = [int(line.strip()) for line in nums]



'''
Selction Sort

We repeat the following process $n-1$ times where $n$ is the length of the array. This is because once there is only one element left, we can assume that it is the largest element of the array.

1. Assign the first unsorted element as the minimum value of the array.
2. For every other unsorted element in the array:
   1. Compare the value of the element with the value we assigned as the minimum
        * If the value of the element is less than the minimum value we assigned:
          * Set this value as the new minimum value
3. Swap the positions of the minimum value with the first unsorted element. 

'''
def SelectionSort(array, asc = True, desc = False):
    # array: array of values to be sorted, assumes each element is an int
    # asc: sort in ascending order, Default: True
    # desc: sort in descending order, Default: False
    
    array = array[:] # so that we don't manipulate the original array.
    
    if desc == True: #descending order
        for i in range(len(array)-1):#repeat $n-1$ times where $n$ is the length of the array.
            max_index = i#Assign the first unsorted element as the maximum value of the array.
            for j in range(i+1,len(array)): #For every other unsorted element in the array:
                    #Compare the value of the element with the value we assigned as the maximum
                    #If the value of the element is greater than the maximum value we assigned
                    if array[j] > array[max_index]:
                        #Set this element as the new maximum elemet
                        max_index = j 
            #Swap the positions of the maximum value with the first unsorted element.
            (array[i], array[max_index]) = (array[max_index], array[i])
    else: #ascending order
        for i in range(len(array)-1):#repeat $n-1$ times where $n$ is the length of the array.
            min_index = i#Assign the first unsorted element as the minimum value of the array.
            for j in range(i+1,len(array)): #For every other unsorted element in the array:
                    #Compare the value of the element with the value we assigned as the minimum
                    #If the value of the element is less than the minimum value we assigned
                    if array[j] < array[min_index]:
                        #Set this element as the new minimum element
                        min_index = j
            #Swap the positions of the minimum value with the first unsorted element.
            (array[i], array[min_index]) = (array[min_index], array[i])
    return array # return the new sorted array
       
'''
Insertion Sort

1. Assume that the fist element, $x_0$ is sorted into it's proper position.
2. For each unsorted element in $X$:
   1. Store the value of $x_i$.
      1. For each of the indices from the last sorted index down to $0$ ($x_j$ through $x_0$):
        * If the $x_j$ is greater than $x_i$:
          * Move $x_j$ to the right by one, $x_j = x_{j+1}$.
        * Insert $x_i$ into the array at the index $j$
'''

def InsertionSort(array, asc = True, desc = False):
    # array: array of values to be sorted, assumes each element is an int
    # asc: sort in ascending order, Default: True
    # desc: sort in descending order, Default: False
    
    array = array[:] # so that we don't manipulate the original array, will just print the sorted array
    
    if desc == True: # decsending
        for i in range(1,len(array)): # starting at index 1 because we assume index 0 is already sorted
            
            x_i = array[i] # The value we are comparing against
            j = i-1 # the highest index in the array that is sorted, starts at 0
            
            # Search sorted indices until we reach the correct position of x_i
            while j >= 0 and array[j] < x_i: 
                array[j + 1] = array[j]  # Shift elements to the right
                j -= 1 # Go to the next sorted element
            array[j+1] = x_i # insert the stored value $x_i$
    
    else: # ascending
        for i in range(1,len(array)): # starting at index 1 because we assume index 0 is already sorted
            
            x_i = array[i] # The value we are comparing against
            j = i-1 # the highest index in the array that is sorted, starts at 0
            
            # Search sorted indices until we reach the correct position of x_i
            while j >= 0 and array[j] > x_i: 
                array[j + 1] = array[j]  # Shift elements to the right
                j -= 1 # Go the the next sorted element
            array[j+1] = x_i # insert the stored value $x_i$
            
    return array # return the sorted array.