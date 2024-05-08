# Hanoi's Tower implementation in python
# Would Like to use stacks for this implementaion:
# Took some inspiration for implementing this on how I have seen other people implement this algorithm, 
# But would like to modify the implementations to store the states of the tower as separate stacks. 
# To make it clearer, I would like each rod to be its own stack and we will move items in the stack (discs)
# between stacks to demonstrate the actual tower of hanoi problem with physical rods and discs. I will store numbers
# in the stacks which will represent the radius of a disc. So each stack will look like as follows at the beginning if we had 3 discs to move
# [1]   []      []
# [2]   []      []
# [3]   []      []
#
# Which after runnning the algorithm would look like:
# []    []      [1]
# []    []      [2]
# []    []      [3]

from cs240functions import Stack as stack

# Some stuff I did while testing:
test1 = stack()
test2 = stack()
test3 = stack()

n = 1

for i in range(n,0,-1):
    test1.push(i)
    test2.push(None)
    test3.push(None)