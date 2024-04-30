#### Binary Search function created during Algorithms Homework 1 - Eric Folsom ####
#### Designed to work over an array or list of integers. Will throw errors if  ####
#### strings and integers mix.                                                 #### 

def binary_search(item, data, oper = False, diag = False):

   # item: item in the data that we are interested in finding
   # data: list or array of data with items we are interested in finding, assumes
   #       ordered integer data
   # oper: Logical T or F. Choose weather to include the number of operations. 
   #        Default: False.
   # diag: T or F. Choose to see the inner workings of the algorithm.
   #        Default: False.

   # Begin by defining some variables for keeping track of x0 and xn
   # as well as keeping track of the number of operations

   x0 = 0 #defining the index of first element of the array
   xn = len(data)-1 #defining the index of the last element of the array
   operations = 0 #creating a varaible to count the number of operations the 

   # Beginning the actual function
   while x0 <= xn: #while we are searching valid indices of our array
      operations = operations + 1 #count one operation
      mid = (xn + x0) // 2 #pick the middle index of the array (floor operation)
      search = data[mid] # Value of the middle index (the one we are searching in)

      #Diagnostics/Inner workings
      #I had to use this a few times to diagnose edge cases
      if diag == True:
        print("Target: ", item,
           '\nLowest Index: ', 
         x0,"\nHigh Index: ",xn,
         "\nIndex we are searching is: ",mid,
          " Value: ",search) 
      
      #if the item we are searching for is the same as the value of the array
      if search == item: 
         #if you want to see the number of operations
         if oper == True: 
            #return the index of the item and the number of
            #  operations it took to find the item
            return print(f"Item {item} is located at index {mid}.\nThis took {operations} operations.")
            #return item, mid, operations 
         else:
            #return the position of the item
            return print(f"Item {item} is located at index {mid}.") 
            #return item, mid, operations 
         
      # if our guess is too low
      elif search < item:
          #update the low index position to be the middle guess. 
          # Adding 1 so we don't recheck the same index twice
         x0 = mid + 1
         #diagnostics
         if diag == True:
           print('Search was too low') #debugging

      # if our guess is too high
      elif search > item: 
         # update the high position to be the middle guess. 
         # Subtracting 1 so we don't check the same index
         # twice, as that would be slow.
         xn = mid - 1 
         #diagnostics:
         if diag == True:
            print("Search was too high") #debugging

   # if we can't find the item in the array.
   return print("Item Not Found\nThis took ", operations, ' operations.') 