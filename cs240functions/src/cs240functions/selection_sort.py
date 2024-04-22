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