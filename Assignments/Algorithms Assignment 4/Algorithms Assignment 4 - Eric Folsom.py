### CS240 Algorithms Assignment 4 - Eric Folsom ###

'''
Quick Sort was a lot easier for me to wrap my head around than merge sort. I was able to get
a good idea on how merge sort was but it would be a lot easier to explain my understanding in a visual form
versus a written form I am afraid. Thinking about the recursion stack as an absolute value function graph
really helped me get a grasp on what was happening in the algorithm and helped me with my pseudocode and implementation.
'''

from cs240functions import binary_search as BinarySearch
from random import sample as sample


## Merge Sort 

def MergeSort(array):
    arr = array[:] # making a copy of the input array so that it remains intact
    
    #the actual merge sort algorithm
    def actualmergesort(arr):
        if len(arr) <2: # if the array has 1 or no elements
            return arr # We have reached the base case
        
        
        
    
    # run the merge sort algorithm on the copy of the input array
    return actualmergesort(arr)
        
    
    


## Quick Sort

def QuickSort(array):
    pass