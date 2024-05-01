# Iterative Linear Search
    
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

# Recursive Linear Search

def LinSearchRec(data, value):

  def searchindex(index): # function to check if a the value is in an index
    if index == len(data): # if we are at the end of the list (base case)
      return print("Item not found") # tell us we couldn't find the item :(
    if data[index] == value: # If we found the item
      return print(f"{value} is located at index {index}") # Tell us where it is
    else: # recursive call
      searchindex(index+1) #search in the next index
  
  searchindex(0) # search starting the list starting at index 0