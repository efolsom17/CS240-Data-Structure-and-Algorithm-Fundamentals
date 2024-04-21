## Importing the numbers-3.txt data

with open("./Data/numbers-3.txt", "r") as nums: #opens the file
    numbers1 = [int(line.strip()) for line in nums]
    
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
  
LinSearchIt(test, 100)
LinSearchRec(test, 100)