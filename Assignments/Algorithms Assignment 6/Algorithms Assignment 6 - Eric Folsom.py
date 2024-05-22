############### Algorithms Assignment 6 - Eric Folsom ################



'''
Implementing a binary search tree in python
 Needs in-order, pre-order, post-order traversal
 Going to need a tree node, similar to the nodes that I created for my linked lists,
 just instead of prev, and next, i'll hae left and right. SHould probably include tree height just so that I can
 easily transition it into an AVL tree. I think a lot of this can be done with recursion. Might try to do this iteratively as well
'''

## Tree Node ##

class TreeNode:
    def __init__(self, data):
        self.data = data # data we want to add to our tree
        self.left = None # starting as None for now
        self.right = None # starting as None for now
        self.height = 1 # height from that node is 1 by default


## Going to need to start with the first data point inserted as the root node, then all the subsequent data
# inputted as child nodes
# Something like, if you insert an array, it would choose the middle index of the array to be the root. then assign nodes
# by the rules of a binary search tree. If you only inputed a single data point, that data would be the root. Or you could make an empty 
# binary search tree. Might be a good idea to assign the first index of the array to be the root, because then we are not assuming that our data is sorted.
        
class BinarySearchTree:
    def __init__(self, data = None):
        # check if data is a single point of data or if it is an array.
        if data is not list: # if the data that we input is not a list
            self.root = TreeNode(data) # assign the root as whatever data we inputed 
        else: # if it is a list
            mid  = len(data)//2
            self.root = TreeNode(mid)# Assign the middle index to be the root of the binary search tree.
            # Call insert function on all the remaining elements
            for i in range(mid): # indices from 0 to mid-1
                pass # this is where the insert function gets called
            for i in range(mid+1,len(data)): # indices from mid+1 to the last index of data
                pass # this is where the insert function gets called
    
    #insert a value into the binary search tree, insert a new node with the given data
    '''
    Start at the root
        If it doesn't exist, then insert the value there
    compare the value at each node
        less than the root, go left
        greater than the root, go right
        do the above until 
    '''
    def insert(self, data):
        # check if the tree is empty
        if self.root is None: # if tree is empty, new node becomes root
            self.root = TreeNode(data)
        # else, the tree already has data
        else:
            #find the correct position for the new node
            current = self.root # start at the root of the tree
            while current:# while current \neq None
                if data < current.data: # if the data is less than the root value:
                    # go to the left subtree
                    if current.left is None: # if there is no left leaf node
                        current.left = TreeNode(data) # create the left leaf node
                        break # stop, we have inserted the data where it belongs
                    current = current.left # traverse to the next node
                
                else: # if the data is greater than or equal to the root node value:
                    # go to the right subtree
                    if current.right is None: # if the right leaf node doesn't exist
                        current.right = TreeNode(data) # create the right leaf node.
                        break # stop we have inserted the data where it belongs
                    current = current.right # go to the next rigth subtree.
    
    # delete a value from the binary serach tree
    '''
    Check if the node is a leaf node, then remove it by removing the link to it
    If the node only has one child node connect the child node the the parent node of the node we are deleting
    if there are both child nodes, find the in-order sucessor, swap values with the node, then delete it.
    '''
    def delete(self, data):
        pass
    
    # helper method to delete a node while keeping binary search tree logic in place
    def _delete_node(self, node, data):
        pass
    # search for a value in the binary search tree (does the tree contain this value or not), might call this contains
    '''
    Start at the root
        if its the value we are looking for return True
        if the value we are looking for is less than the root, continue searching the left subtree
        if the value we are looking for is greater than the root, searhc the right subtree
        Eventually if we don't find the value after searching the whole tree, return False 
    '''
    def contains(self, node, data):
        pass
    
    # find the minimum value (.min)
    '''
    traverse all the way to the left and return the value
    '''
    def getmin(self, node):
        pass
    
    # find the maximum value (.max)
    '''
    traverse all the way to the right and return the value
    '''
    def getmax(self, node):
        pass
    
    # pre order traversal
    '''
    Visit root node first
    Recursively do a pre-order traversal of the left subtree
    recursively do a pre-order traversal of the right subtree
    'pre' because we visit the node before the recursive traversal of the subtrees
    '''
    def preOrder(self, node):
        pass
    
    # in order traversal
    '''
    recursively do an in-order traversal of the left subtree
    visit the root node
    recursively do an in-order traversal of the right subtree
    
    'in-order' because we recursively traverse the left subtree, then visit the middle (root), then traverse the right subtree
    '''
    def inOrder(self, node):
        pass
    
    
    # post order traversal.
    '''
    recursively do post-order traversal of the left subtree
    recursively do post-order traversal of the right subtree
    visit the root node
    "post" because we visit the root node after traversing both subtrees.
    '''
    def postOrder(self, node):
        pass
            
