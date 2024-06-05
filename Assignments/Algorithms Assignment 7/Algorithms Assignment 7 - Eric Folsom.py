###  CS240 Algorithms Assignment 7 - Eric Folsom ###

'''
Heap Data structure that has heap sort and heap search (need to clarify if the search is for any value or if its for the min and max values).


My idea for a search implementation would be to do heap sort until the value that we are extracting is the value we are searching for, and then if we have ran heap sort on the entire array, and the value didn't come up, we
decide that the value is not found in our heap.

Going to build a max-heap. Special complete binary tree where for a given node, the value at that node will be greater than the values in its child node. The maximum value in the max-heap is the root.

I am going to use the array implementation of the binary tree, because it seems to be an elegant implementation, and because I think that my BST and AVL tree implementations were'nt the greatest,
and probably aren't the most useable in this context. 

Using the relationship between array indexes and tree elements:

For a given index , "i", the left child node of element "i" is in index "2i+1", and the right child node of element "i" is in index "2i+2" 

So for that I will need:
heapify - creates a heap from a node, ran on all non-leaf elements of the heap, recursive function.
build_max_heap - builds a max-heap from an array. calls heapify
heapsort - continually builds a max-heap, then places the root node at the end of the array and then continues the same process with an array one smaller. Do this until the whole array is sorted.

heapSearch - Do Heapsort, but when we extract the root element, compare the value of the root to the value we are searching for, if it is the value we want, return true, else do heapify on the rest of the array and if nothing is found return FAlse.
    EVEN BETTER, HEAPSORT into like Binary Search since we have a sorted array.
    Decided for this to modify my heapsort function. After we sort an element, we compare the element with the value we are searching for, if we can't find it we continue heapifying the array.
    

Resources used:
    Videos from Canvas: the 3 and 6 minute videos on Heaps were very helpful in my understanding of how heaps functioned and their operations.
    https://www.programiz.com/dsa/heap-data-structure: Nice reading on heaps and also helps with understanding the heapSort function. 
        There are nice graphics that help break down what is going on at each step of the process
        https://www.programiz.com/dsa/heap-sort, spefically for the sort portion. 
        
'''
import random # testing purposes



## Heapify - Takes in an Array

def heapify(array, n, i): 
    # array: array storing the data in our heap
    # n: length of the array
    # i: index of the root we are heapifying
    large = i # set the largest value to be index i (root)
    left = 2 * i + 1 # left child of node i (index)
    right = 2 * i + 2 # right child of node i (index)
    
    
    # finding the largest value among the root and its children
    if left < n and array[large] < array[left]: # if left index is still within the bounds of the array AND the value at index i is less than its left child node's value
        large = left # set the large node to be the index of node i's left child
    
    if right < n and array[large] < array[right]: # if the right index is still within the bound of the array AND the value at index i is less than its right child node
        large = right # set the large node to be the index of node i's right child
    
    
    if large != i: # if the root is not the largest value
        array[i], array[large] = array[large], array[i] # swap the root with the largest value
        heapify(array, n, large) # continue heapifying on the new root node

# build max heap from an array
def build_max_heap(arr):
    n = len(arr) # set n as the 
    
    for i in range( (n//2) - 1, -1,-1):
        heapify(arr, n, i)
    
def HeapSort(arr):
    arr = arr[:] # keep the original array intact, work with a copy of the original array
    build_max_heap(arr)
    
    for i in range(len(arr)-1, -1, -1):
        # swap elements
        arr[i], arr[0] = arr[0], arr[i]
        # after we swap the elements, they are in sorted positions
        # index 0 is the root of the max heap which is the largest value, so we swap it with index i (counting down, so i is at the end of the array.)
        # now that that value is in the correct position, we call heapify on the new "root" ( index 0 ), to get the largest remaining value in index 0, so we can swap.
        # heapify the root
        heapify(arr, i, 0)
    return arr # return the sorted array

def HeapSearch(arr, value): # does it contain the value, could try and modify the heapsort function, 
    # or I could just heapsort into binary search...(my binary search implemention needs to be modified to do this, wont do this method)
    arr = arr[:] # keep the original array intact, work with a copy of the original array
    build_max_heap(arr)
    
    for i in range(len(arr)-1, 0, -1):
        # swap elements
        arr[i], arr[0] = arr[0], arr[i]
        # compare the value that we just swapped into the correct position with the value we are searching for
        if arr[i] == value: # if the value we just sorted equals the value we are looking for
            return True # return True, the heap does contain the value we are looking for
        else: # else if the value we just sorted does not the qual the value we are looking
            heapify(arr, i, 0) # continue heapifying on the new root root.
    return False # sorted the array fully and we did not find the item we were looking for

def getminHeap(arr): # heapsort the array then return the value index 0
    arr = HeapSort(arr)
    return arr[0] 

def getmaxHeap(arr): # create a max heap from the array and extract the root
    arr = arr[:]
    build_max_heap(arr)
    return arr[0]


#### Testing / Demonstration ####
random.seed(1234567890)
test = [random.randint(1, 50) for _ in range(25)]
print(f"Random array: {test}")
# building a max heap from the random array
build_max_heap(test)
print(f"Array as a Heap: {test}")
# Searching the heap
print(f"Contains 11: {HeapSearch(test, 11)}")
print(f"Contains 10: {HeapSearch(test, 10)}")
print(f"Min: {getminHeap(test)}")
print(f"Max: {getmaxHeap(test)}")
# Sorting
print(f"Sorted array using HeapSort: {HeapSort(test)}")