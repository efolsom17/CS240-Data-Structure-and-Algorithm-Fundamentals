# CS240 Spring 2024 Midterm - Eric Folsom
# Hanoi's Tower implementation in python

from cs240functions import Stack as stack

'''
Recursive implementation
'''

# Basic implementation
def tower_of_hanoi(n, starting_rod, middle_rod, ending_rod): # specify the starting rods you want
    if n == 1: # Base case
        print(f"Disk {n}: {starting_rod} -> {ending_rod}") # Move the specified disk 
    else: # if we are not on the last rod
        tower_of_hanoi(n-1, starting_rod, ending_rod, middle_rod) # recursive call to move the n-1 disks to the middle rod using the ending rod as the axullary rod
        print(f"Disk {n}: {starting_rod} -> {ending_rod}") # move the current disk
        tower_of_hanoi(n-1, middle_rod, starting_rod, ending_rod) # move the remaining n-1 disks to the ending rod using the starting rod as the auxillary rod


# Implementation using stacks
# This was an attempt at making a nice visual representation of the stacks of disks on each rod, didn't turn out as well as I hoped


# function to move the top value of stack 1 to the top of stack 2
def moveStack(stack1 = stack(), stack2 = stack()):
    temp = stack1.pop()
    stack2.push(temp)

# tower of of hanoi recursive solution that works on the stacks 
def tower_of_hanoi_stacks(n, starting_rod, middle_rod, ending_rod): # specify the starting rods you want
    if n == 1: # Base case
        moveStack(starting_rod, ending_rod)
        print(f"AFTER\nStarting Rod:\n{starting_rod}\nAuxilary Rod:\n{middle_rod}\nEnding Rod:\n{ending_rod}\
        \n Moved disk {n}")
    else: # if we are not on the last rod
        tower_of_hanoi_stacks(n-1, starting_rod, ending_rod, middle_rod) # recursive call to move the n-1 disks to the middle rod using the ending rod as the axullary rod
        moveStack(starting_rod, ending_rod) # move the current disk
        print(f"AFTER\nStarting Rod:\n{starting_rod}\nAuxilary Rod:\n{middle_rod}\nEnding Rod:\n{ending_rod}\
        \n Moved disk {n}")
        tower_of_hanoi_stacks(n-1, middle_rod, starting_rod, ending_rod) # move the remaining n-1 disks to the ending rod using the starting rod as the auxillary rod


def TowerOfHanoi(n):# Tower of Hanoi with stacks and it will initialize the number of disks
    # n = number of disks
    
    ## initialize the starting, auxillary, and ending rods
    
    starting_rod = stack()
    auxillary_rod = stack()
    ending_rod = stack()
    
    # fill the starting rod
    for i in range(n,0,-1):
        starting_rod.push(i)
    
    # display starting state
    print("Start:")
    print(f"Starting Rod:\n{starting_rod}\nAuxillary Rod:\n{auxillary_rod}\nEnding Rod:\n{ending_rod}")
    
    # now we can call the tower of hanoi function. It will print its final state
    
    tower_of_hanoi_stacks(n, starting_rod, auxillary_rod, ending_rod)
    


'''
Iterative implementation
'''

# Function to move disks between to rods

def moveDisk(start, end, s , e): # start and end are both stacks, s and e are labels for the stacks
    # get the top value of each stack
    topstart = start.pop() 
    topend = end.pop()
    
    # compare values to determine valid movements
    
    # if start is empty
    if topstart == None: # if start rod is empty
        start.push(topend) # move the disk on the end rod to the start rod (only valid move)
        print(f"Disk {topend}: {e} -> {s}") # display the move
    
    # if end is empty
    elif topend == None: # if the end rod is empty
        end.push(topstart) # move disk on start rod to end rod (only valid move)
        print(f"Disk {topstart}: {s} -> {e}") # dispaly the move
        
    # compare the values and move them accordingly, 
    elif topstart > topend: # disk on top of starting rod is bigger than disk on ending rod
        # move disk on end rod to start rod ( only valid move between the two rods)
        start.push(topstart) # put the top value of start back onto the rod
        start.push(topend) # put the top value of end on top of the start rod
        print(f"Disk {topend}: {e} -> {s}") # display the move
    else: #disk on top of starting rod is smaller than the disk on the ending rod
        # move the disk on the start rod to the end rod ( only valid move between the two rods)
        end.push(topend) # put the top value of end back onto the end rod
        end.push(topstart) # put the top value of start on top of the end rod
        print(f"Disk {topstart}: {s} -> {e}") # display the move
        
# Iterative implementation using moveDisk()

def tower_of_hanoi_it(n, start, aux, end):
    # initialize stacks
    start = stack(n)
    aux = stack(n)
    end = stack(n)
 
    
    # fill in starting stack (rod)
    for i in range(n,0,-1):
        start.push(i)
    
    #labels for printing
    s, a, e = 'Start', 'Aux', 'End'
    
    # check if n is even or odd, have to change some things if that is the case
    if (n % 2 == 0):
        # swap auxilary and end rods, the first step that will be made ( so we are moving disks between the correct rods)
        temp = e 
        e = a
        a = temp
    
    
    
    #iterate through the number of moves
    for i in range(1,int(2**n)): # range 1 to 2^n-1, but because of how python's range function works we can just write 2^n
        if (i % 3 == 1): # valid move between start and end rod (start and auxillary if n is even)
            moveDisk(start, end, s, e) # function to move the rods
        elif (i % 3 == 2): # valid move between start and auxillary rod (start and end if n is even)
            moveDisk(start, aux, s, a) # function to move the rods
    
        elif (i % 3 == 0): # valid move between auxillary and end rod
            moveDisk(aux, end, a, e) # funciton to move the rods

'''
Variation where the number of rods is varied instead of the number disks
'''

def THanoiG3R(n): # number of rods, done with three disks.
    
    if n <3:
        return f"Puzzle must have at least 3 pegs"
    if n == 3:
        return tower_of_hanoi(3, "Start", "Auxillary", "End")
    if n > 3:
        nopen = n -1 
        auxopen = nopen-1
        print(f"Disk 1: Start -> Auxillary ({auxopen} available)")
        auxopen -= 1
        print(f"Disk 2: Start -> Auxillary ({auxopen} available)")
        print(f"Disk 3: Start -> End")
        print(f"Disk 2: Auxillary -> End")
        print(f"Disk 1: Auxillary -> End")


