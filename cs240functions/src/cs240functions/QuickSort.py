from random import sample as sample

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
