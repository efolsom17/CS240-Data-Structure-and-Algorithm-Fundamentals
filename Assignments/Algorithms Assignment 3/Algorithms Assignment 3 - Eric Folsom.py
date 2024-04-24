## Importing the numbers-3.txt data

with open("./Data/numbers-3.txt", "r") as nums: #opens the file
    numbers3 = [int(line.strip()) for line in nums]
    
from random import sample

test = sample(list(range(100)),100)    

def LinSearchIt(data, value): # iterative linear serach, takes in data as a list of integers
    searches = 0# to tell us if we are out of the array
    for i in range(len(data)-1): # for every index in the array
        if value == data[i]: # compare the value of x_i with x_j
            searches += 1
            return print(f"{value} is located at index {i} \nThis took {searches} searches.") # tell us if we find the value or not,
        # go to the next index and compare
        else:
           searches+= 1
    return print(f"Item Not Found \nThis took {searches+1} searches.")# if its not found it won't loop thorugh the one last time to update searches, the searches+1 corrects this


def LinSearchRec(data, value):

  def searchindex(index):
    if index == len(data):
      return print("Item not found")
    if data[index] == value:
      return print(f"{value} is located at index {index}")
    else:
      searchindex(index+1)
  
  searchindex(0) # search starting the list starting at index 0
  
def BinarySearchRec(data, item = int, low = 0, high = None):
  
  #set high to be the highest index in the array/list
  if high is None: # default, will set the last index as the highest index
    high = len(data)-1

  if low > high: # if we are outside the bounds of the list 
    return "Item Not Found"
  
  mid = (high+low) //2 # define the middle index

  if data[mid] == item: # base case, we find the item at the middle index
    return print(f"{item} is located at index {mid}") #tell us where the item is

  elif item < data[mid]: # if our item we are searching for is less than the middle item
    return BinarySearchRec(data, item, low, mid-1) # search the left(bottom) half of the list
    
  else: # if the item we ar seraching for is greater than the middle item
    return BinarySearchRec(data, item, mid+1, high) #search the right(top) half of the list.



#### testing ####  
LinSearchIt(test, 10)
LinSearchRec(test, 10)

from cs240functions import InsertionSort
from cs240functions import binary_search

test = InsertionSort(test)

LinSearchRec(test,10)
BinarySearchRec(test,10)
binary_search(10,test)