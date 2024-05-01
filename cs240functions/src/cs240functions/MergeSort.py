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
        
    