## Algorithms Assignment 2 - Eric Folsom ##

from random import sample as sample
from random import randint as rdunif

## Importing the numbers-1.txt data

with open("./Data/numbers-1.txt", "r") as nums: #opens the file
    numbers1 = [int(line.strip()) for line in nums]

test_numbs = list(range(100))
test_numbs = sample(test_numbs, len(test_numbs))

'''
Selction Sort
'''
def SelectionSort(array, asc = True, desc = False):
    # array: array of values to be sorted, assumes each element is an int
    # asc: sort in ascending order, Default: True
    # desc: sort in descending order, Default: True
    temp_array = array[:]
    
    if desc == True: #descending order
        for i in range(len(temp_array)-1):#repeat the following process $n-1$ times where $n$ is the length of the array.
            max_index = i#Assign the first unsorted element as the maximum value of the array.
            for j in range(i+1,len(temp_array)): #For every other unsorted element in the array:
                    #Compare the value of the element with the value we assigned as the minimum
                    if temp_array[j] > temp_array[max_index]:#If the value of the element is greater than the maximum value we assigned
                        max_index = j#Set this value as the new maximum value
            (temp_array[i], temp_array[max_index]) = (temp_array[max_index], temp_array[i])#Swap the positions of the maximum value with the first unsorted element.
    else: #ascending order
        for i in range(len(temp_array)-1):#repeat the following process $n-1$ times where $n$ is the length of the array.
            min_index = i#Assign the first unsorted element as the minimum value of the array.
            for j in range(i+1,len(temp_array)): #For every other unsorted element in the array:
                    #Compare the value of the element with the value we assigned as the minimum
                    if temp_array[j] < temp_array[min_index]:#If the value of the element is less than the minimum value we assigned
                        min_index = j#Set this value as the new minimum value
            (temp_array[i], temp_array[min_index]) = (temp_array[min_index], temp_array[i])#Swap the positions of the minimum value with the first unsorted element.
    return temp_array
       
'''
Insertion Sort
'''