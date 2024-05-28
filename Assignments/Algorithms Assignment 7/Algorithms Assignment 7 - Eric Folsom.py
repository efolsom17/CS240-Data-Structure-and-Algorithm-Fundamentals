###  CS240 Algorithms Assignment 7 - Eric Folsom ###

'''
Heap Data structure that has heap sort and heap search.

Should also include insertion and deletion probably, as well as the min and max values.

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
'''

## Heapify - Takes in an Array

def heapify(array, n, i): 
    # array: array storing the data in our heap
    # n: length of the array
    # i: index
    large = i # set the largest value to be index i (root)
    left = 2 * i + 1 # left child of node i
    right = 2 * i + 2 # right child of node i
    
    
    # finding the largest value among the root and its children
    if left < n and array[i] < array[left]: # if left index is still within the bounds of the array AND the value at index i is less than its left child node
        large = left # set the large node to be the index of node i's left child
    
    if right < n and array[i] < array[right]: # if the right index is still within the bound of the array AND the value at index i is less than its right child node
        large = right # set the large node to be the index of node i's right child
    
    
    if large != i: # if the root is not the largest value
        array[i], array[large] = array[large], array[i] # swap the root with the largest value
        heapify(array, n, large) # continue heapifying on the new root node

# build max heap from an array
def build_max_heap(arr):
    n = len(arr) # set n as the 
    
    for i in range(n//2, -1,-1):
        heapify(arr, n, i)
    
def HeapSort(arr):
    pass

def HeapSearch(arr, value):
    pass