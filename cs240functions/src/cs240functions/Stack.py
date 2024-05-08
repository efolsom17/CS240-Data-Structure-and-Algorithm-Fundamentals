class Stack:
    # Initializing the stack, size is how big you want the stack to be, hope to find a way to make an unspecified size stack, maybe this does this for me, we'll see
    def __init__(self, size = int):
        self.stack = [] # initializing the stack as an array
        self.size_limit = size # setting the "size limit" of the stack
        self.size = len(self.stack)
    
    # push
    def push(self, item): # item is whatever you want to put onto the stack.
        if self.IsFull(): # if we can no longer fit items in the stack
            return print("Stack is full")
        else:
            self.stack.append(item) # appends the stack array
            self.size += 1 # update the size of the stack
    
    # pop
    def pop(self): # read and remove the top item of the stack
        if self.IsEmpty(): # Check if the Stack is empty
            return print("Stack is empty")
        # If the stack contains items
        self.size -= 1
        return self.stack.pop() # Because we are using an array to implement our stack, we can use python's built in pop function on arrays.
    
    # IsEmpty
    def IsEmpty(self): # is the stack empty
        return len(self.stack) == 0 # IsEmpty is True if len(self.stack) is 0
    
    # IsFull
    def IsFull(self): # is the stack full
        return len(self.stack) == self.size_limit # IsFull is True if len(self.stack) equals the specified size limit
    
    # Peek 
    def peek(self): # take a peek a the end of the stack
        if self.IsEmpty(): # if the stack is empty
            return print("Stack is empty") # tell us
        return self.stack[-1] # read the last index in the stack array.
    
    def __repr__(self):
        # Create a visual representation of the stack
        return '\n'.join(['| {} |'.format(item) for item in reversed(self.stack)]) + '\n-------'