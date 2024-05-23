#### CS240 Data Structures Assignment 4 - Eric Folsom ####

'''
Mostly going to adapt the work that I have done on BST to include the height of the tree and the balance factor

Resources used:

https://en.wikipedia.org/wiki/AVL_tree: Very good for pseudocode and for breaking down the algorithm. Also good for general information on the AVL trees.
https://www.w3schools.com/dsa/dsa_data_avltrees.php: Another good resource which explains the different rotations and the four "out of balance" cases
https://www.programiz.com/dsa/avl-tree: I really liked their implementation, as it involves a class like I had with my BST, using this a my main source of inspiration for implementing
an AVL tree in python.
ChatGPT: Used for help on implementing things in python and debugging. I am starting to find ChatGPT very helpful for creating tests for my code. I can prompt it by giving it my code and asking it to provide some tests for my code.
 
'''

## Tree Node ##

class TreeNode:
    def __init__(self, data):
        self.data = data # data we want to add to our tree
        self.left = None # starting as None for now
        self.right = None # starting as None for now
        self.height = 1 # adding this compared to BST implementation, will be used to balance the trees

## AVL Tree Class

'''
Things from an AVL tree that we don't have in a BST

Balance factor:
    Balance factor for a node is the diffreence in the height between its left and right subtrees
        0, node is in balance
        more than 0, right heavy
        less than 0, left heavy
        
    If |balance factor| > 1, then the tree is not balanced and we need to perform a rotation operation to rebalance the tree.
    
Will need a function to keep track of the balance factor
    
Out of Balance Cases, that require rotations (getting these from w3schools)
    Left-Left: The unbalanced node and its left child node are both left-heavy -> single right rotation
    Right-Right: The unbalanced node and its right child node are both right-heavy -> single left rotation
    Left-Right: The unbalanced node is left heavy, and its left child node is right heavy -> Left rotation on the left child node, then right rotaion on the unbalanced node
    Right-Left: The unbalanced node is right heavy, and its right child node is left heavy -> Right rotation on the right child node, then left rotation on the unbalanced node
    
Will need functions to perform the required rotations.
'''
        
class AVLTree():
    def __init__(self, data = None):
        self.root = None
        if data: # if data \neq None
            # insert the data into the new AVLTree
            for item in data:
                self.insert(item)
    
    # Insert data into the AVL tree, going to use a helper method like i did with bst            
    def insert(self, data):
        self.root = self._insert_node(self.root, data) #  call our helperfunction to insert the data starting at the root of the tree.
    
    # helper method for the insert
    def _insert_node(self, node, data):
        # find the correct position of the node
        if node is None: # if there is no data at the node, base case
            return TreeNode(data)  # insert the node as the data
        # if the value we are inputing is less than the value of the data at the current node
        if data < node.data:
            node.left = self._insert_node(node.left, data)# recursive call on the left subtree
        else: # value we are inputing is greater than the value of the data at the current node
            node.right = self._insert_node(node.right, data) # recursive call on the right subtree
        
        # updating the height
        node.height = 1 + max(self.getHeight(node.left), self.getHeight(node.right))
        
        # Balance factor
        balanceFactor = self.getBalanceFactor(node)
        
        # Rotations, from w3schools
        
        
            # Left Left
        if balanceFactor > 1 and data < node.left.data:
            return self.rightRotate(node)

        # Right Right
        if balanceFactor < -1 and data > node.right.data:
            return self.leftRotate(node)

        # Left Right
        if balanceFactor > 1 and data > node.left.data:
            node.left = self.leftRotate(node.left)
            return self.rightRotate(node)

        # Right Left
        if balanceFactor < -1 and data < node.right.data:
            node.right = self.rightRotate(node.right)
            return self.leftRotate(node)
        
        return node
        
    # Delete Node
    
    def delete(self, data):
        # call the _delete_node method starting at the root node.
       self.root = self._delete_node(self.root, data)
    
    # helper method to delete a node while keeping binary search tree logic in place
    def _delete_node(self, node, data):
        if node is None: # Check if the node is empty
            return node # Returns None if the node we are trying to delete is empty
        # Theses are basically to get us to the place in the tree where the value we want do delete is located
        if data < node.data: #if the value we want to delete is less than the node data
            # go to the left subtree 
            node.left = self._delete_node(node.left, data) # recursive call on the left subtree to delete the value
        elif data > node.data: # If the value we want to delete is greter than the node data
            # go to the right subtree
            node.right = self._delete_node(node.right, data) # recursive call on the right subtree to delete the value
        # once we find the node with the data we want to delete
        else: 
            # nodes with only one child node
            
            # No left child node
            if node.left is None:
                return node.right # Replace the node with its right child node
            # No right child node
            elif node.right is None:
                return node.left # Replace the node with its left child node
            
            # Node with both child nodes
            # get get the in order sucessor, smallest value in the right subtree 
            temp = self._minNode(node.right) # getting the min value from the right subtree ( i.e value just greater than the value we are deleting)
            # copy the data of the in order sucessor to the node
            node.data = temp.data
            # delete in order sucessor
            node.right = self._delete_node(node.right, temp.data)
            
        '''
        Height, balance, and rotation stuff goes here.
        '''
             
        return node # returns the updated node
    
    # Funciton to perform a left rotation
    def leftRotate(self, x): # x is the node that we are performing the rotation on
        pass
    
    # funciton to perform a right rotation
    def rightRotate(self, x): # x is the node that we are performing the rotation on
        pass
    
    # function to get the height of a node
    def getHeight(self, node):
        if node is None: # if the node has no data, 
            return 0 # set the height of the node to 0
        return node.height #  else return the height of the node.
    
    # Function to get the balance factor of a node
    def getBalanceFactor(self, node):
        # balance factor is the height of left subtree - height of right subtree
        if node is None:
            return 0
        return self.getHeight(node.left)-self.getHeight(node.right)
   
   ##### FUNCTIONS THAT I AM REUSING FROM BST , they don't make any changes to the tree.
    
    # helper method to get the node with the minimum value in a given subtree
    def _minNode(self, node):
        current = node # start at the given node
        while current.left is not None: # while the node that we are at has a left leaf node
            current = current.left # keep traversing down the left
        return current # return the node that we stop at
    
    
    # search for a value in the binary search tree (does the tree contain this value or not), might call this contains
    '''
    Start at the root
        if its the value we are looking for return True
        if the value we are looking for is less than the root, continue searching the left subtree
        if the value we are looking for is greater than the root, searhc the right subtree
        Eventually if we don't find the value after searching the whole tree, return False 
    '''
    def contains(self, data):
        # start at the root of the bst
        current = self.root
        # traverse the tree
        while current: # while current \neq None
            if data == current.data: # if we find the value we want to find
                return True # return True
            elif data < current.data: # if the value we are searching for is less than the value of the current node
                # traverse the left of the tree
                current = current.left
            else: # if the value we are searching for is greater than the value of the current node
                current = current.right # traverse the right side of the tree
        # if we search all the way and we haven't found the value, i.e, Current == None
        return False # False, the BST does not contain the value
            
    # find the minimum value (.min)
    '''
    traverse all the way to the left and return the value
    '''
    def getmin(self):
        if self.root is None: # check if the root exists
            return None #  if it doesn't return None
        # root exists
        current = self.root
        # traverse the left of the tree
        while current.left: # while current.left \neq None
            current = current.left # continue traversing to the left
        return current.data # return the value of the last node in the left subtree
    
    # find the maximum value (.max)
    '''
    traverse all the way to the right and return the value
    '''
    def getmax(self):
        if self.root is None: # check if the root exists
            return None # if it doesn't return None
        # Root exists, traverse the right subtree
        current = self.root
        # traverse the right of the tree
        while current.right: # while current.right \neq None
            current = current.right # continue traversing the right subtree
        return current.data #  return the value of the last node in the right subtree
   
    
    
    
    # TRAVERSAL METHODS - COPIED FROM BST
    
    
    # pre order traversal
    '''
    Visit root node first
    Recursively do a pre-order traversal of the left subtree
    recursively do a pre-order traversal of the right subtree
    'pre' because we visit the node before the recursive traversal of the subtrees
    '''
    def preOrder(self):
        # root, left, right
        result = [] # array for storing and printing traversal
        self._preOrder(self.root, result) # call our helper function starting at the root node
        return result # return the result array
    
    def _preOrder(self, node, result): # node is starting node, result is the storage array to store the results of our traversal
        if node is None: # if the starting node is empty (base case)
            return # stop, go up one layer in the recursive stack
        result.append(node.data) # add the starting (root) node to the results array, doing this instead of printing it as im trying to make this a class for some reason
        self._preOrder(node.left, result) # recursive preOrder traversal on the left subtree
        self._preOrder(node.right, result) # revursive preOrder traversal on the right subtree 
    
    # in order traversal
    '''
    recursively do an in-order traversal of the left subtree
    visit the root node
    recursively do an in-order traversal of the right subtree
    
    'in-order' because we recursively traverse the left subtree, then visit the middle (root), then traverse the right subtree
    '''
    def inOrder(self):
        # left, root, right
        result = [] # array for storing and printing traversal
        self._inOrder(self.root, result) # call our helper function starting at the root node
        return result # return the result array
    
    def _inOrder(self, node, result):# node is starting node, result is the storage array to store the results of our traversal
        if node is None: #  if the starting node is empty, base case
            return # stop, go up one layer in the recursive stack
        self._inOrder(node.left, result) # recursive call on the left subtree
        result.append(node.data) # add the node data to the result array
        self._inOrder(node.right, result) # recursive call on the right subtree
    
    # post order traversal.
    '''
    recursively do post-order traversal of the left subtree
    recursively do post-order traversal of the right subtree
    visit the root node
    "post" because we visit the root node after traversing both subtrees.
    '''
    def postOrder(self):
        # left, right, root
        result = [] # array for storing and printing traversal
        self._postOrder(self.root, result) # call our helper function starting at the root node
        return result # return the result array
    
    def _postOrder(self, node, result):# node is starting node, result is the storage array to store the results of our traversal
        if node is None: # if the startiung node is empty, base case
            return # stop, go up one layer in the recursive stack
        self._postOrder(node.left, result) #  recursive call on the left subtree
        self._postOrder(node.right, result) # recursive call on the right subtree
        result.append(node.data) # add the node data to the results array
