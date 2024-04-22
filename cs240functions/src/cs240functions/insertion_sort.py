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