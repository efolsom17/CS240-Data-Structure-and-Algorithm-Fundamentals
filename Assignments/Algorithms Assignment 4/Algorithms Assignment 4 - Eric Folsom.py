### CS240 Algorithms Assignment 4 - Eric Folsom ###

'''
Quick Sort was a lot easier for me to wrap my head around than merge sort. I was able to get
a good idea on how merge sort was but it would be a lot easier to explain my understanding in a visual form
versus a written form I am afraid. Thinking about the recursion stack as an absolute value function graph
really helped me get a grasp on what was happening in the algorithm and helped me with my pseudocode and implementation. 
I used w3schools, programiz, Skiena, geeksforgeeks, various youtube videos, and some ChatGPT as resources
which helped me implement and understand the merge sort algorithm. 
The largest challenge I faced with quick sort was actually a python thing which was going through all elements besides one in an array.
This is easy for me to implement in R, but I had to use some help to accomplish it in python, as I wanted to 
choose a random pivot for each sub array.
'''

from cs240functions import binary_search as BinarySearch
from random import sample as sample


## Merge Sort 

def MergeSort(array):
    arr = array[:] # making a copy of the input array so that it remains intact
    
    #the actual merge sort algorithm
    def actualmergesort(arr):
        if len(arr) <= 1: # if the array has 1 or no elements (assumed to be sorted)
            return arr # We have reached the base case, return the single element array to be merged.
        
        #choose the middle index of the array
        middle = len(arr)//2 # floor function so we get an integer
        # Split the array in half recursively on the halves of the array to the left and right of the middle index
        left = actualmergesort(arr[:middle])# indices of the array to left of the middle
        right = actualmergesort(arr[middle:])# indices of the array to the right and including the middle
        
        # Merging the two halves of the arrays
        # storing indicies, i = left, j = right, k = array to be merged and sorted
        i = j = k = 0 # start at the beginning
        while i < len(left) and j < len(right): # while we are still looking at elements from both the right and left half,
            # compare the elements
            if left[i] < right[j]:  # if the value of the index we are at in the left half is less than the value of the index we are at in the right half,
                arr[k] = left[i] # put it into its proper place in the merged array
                i += 1 # go the the next index of the left half
            else:  # if the value of the index we are at in the right half is less than or equal to the value of the index we are at in the left half,
                arr[k] = right[j] # put it into its proper place in the merged array
                j += 1 # go the the next index of the right half
            k += 1 # go to the next index that we want to put a value into in the merged array
        
        # add any of the remaining elements in the left or right half to the merged array if there are any left
        while i < len(left): # while we are still in the left half, if any elements remain in the left half
            arr[k] = left[i] # add that value to the merged array
            i += 1 
            k += 1
        while j < len(right): #while we are still in the right half, if any elements remain in the right half
            arr[k] = right[j] # add the element to the merged array  
            j += 1
            k += 1 
        return arr # return the merged and sorted array
    # run the merge sort algorithm on the copy of the input array
    actualmergesort(arr)
    # return the sorted copy array, so that the original is intact
    return arr
        
    
    


## Quick Sort

def QuickSort(array):
    # Making a copy of the array so that we keep the original intact
    arr = array[:]
    # actual quicksort function
    def actualquicksort(arr):
        #define base case
        if len(arr) <= 1: # array is size 1 or less (assumed to be sorted)
            return arr # return sorted array
        else: # if the array cannot be assumed sorted (more than 1 or 0 elements)
            pivot_index = int(sample(range(len(arr)),1)[0]) # choose a random index in the array as the pivot index
            pivot = arr[pivot_index] # Choose our pivot index
            
            # partition the array into values less than, greater than, and equal our pivot and store them
            
            # Less than the pivot
            less = [ item for item in arr if item < pivot] # store the item if it is less than the pivot
            # Equal to the pivot (kinda need this since im choosing a random index for my pivot)
            equal_to = [ item for item in arr if item == pivot] # stores the item if it equals the pivot
            # Greater than the pivot
            greater = [item for item in arr if item > pivot] # stores the item if it is greater than the pivot
            # Recursively sort the remaining partitions and join everything together.
            return actualquicksort(less) + equal_to + actualquicksort(greater)
    
    return actualquicksort(arr) # do the quicksort on the copy of the array that we inputed
    
            
            
          

#Verification/testing:

## Importing the numbers-4.txt data

with open("./Data/numbers-4.txt", "r") as nums: #opens the file
    numbers4 = [int(line.strip()) for line in nums]
    
test = sample(range(100),100)

numbers4_sorted_merge = MergeSort(numbers4)
numbers4_sorted_quick = QuickSort(numbers4)

BinarySearch(90262, numbers4_sorted_merge)
BinarySearch(90262, numbers4_sorted_quick)
BinarySearch(11559, numbers4_sorted_merge)
BinarySearch(11559, numbers4_sorted_quick)