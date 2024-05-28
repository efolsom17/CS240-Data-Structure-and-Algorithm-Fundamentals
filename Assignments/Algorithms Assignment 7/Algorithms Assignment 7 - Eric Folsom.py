###  CS240 Algorithms Assignment 7 - Eric Folsom ###

'''
Heap Data structure that has heap sort and heap search.

Should also include insertion and deletion probably.

My idea for a search implementation would be to do heap sort until the value that we are extracting is the value we are searching for, and then if we have ran heap sort on the entire array, and the value didn't come up, we
decide that the value is not found in our heap.

Going to build a max-heap. Special complete binary tree where for a given node, the value at that node will be greater than the values in its child node. The maximum value in the max-heap is the root.

I am going to use the array implementation of the binary tree, because it seems to be an elegant implementation, and because I think that my BST and AVL tree implementations were'nt the greatest,
and probably aren't the most useable in this context. 

Using the relationship between array indexes and tree elements:

For a given index , "i", the left child node of element "i" is in index "2i+1", and the right child node of element "i" is in index "2i+2" 

So for that I will need:
heapify - creates a heap from a node, ran on all non-leaf elements of the heap, recursive function.
build_max_heap - builds a max-heap from an array.
'''