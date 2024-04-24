## Algorithms Assignment 3 - Eric Folsom ##

# The two search functions below were basically my pseudocode for the
# iterative and recursive linear search implementations in python.

# Iterative Linear Search

LinSearchIt <- function(data, value){ # data is assumed to be a vector
  
  n <- length(data)
  for(i in 1:n) { # loops through the indices of our vector until we find the value we are looking for 
    if(value == data[i]){ # if the value we are looking for is the value in the index we are searching
      return(paste0( value, " is located at index ", i)) # return the value and its index
    } # go to the next index.
  }
}


# Recursive Linear Search

LinSearchRec <- function(data, value){ #Data is assumed to be a vector
  
  checkequal <- function(index){ # function to check if values in an array are equal to some value
    if(index > length(data)) # if we are outside of the valid indices of our vector. 
      break() # stop
    if(data[index] == value){ # if we find the value we are looking for
      return(paste0( value, " is located at index ", index)) # tell us where it is
    }
    else{ # if we didn't find it
      checkequal(index+1) # check the next index
    }
  }
  checkequal(1) # starts us searching the vector, starts at index 1 because this is R.
}




# Previous For Loop as a recursive function

#testing Recursive K-means stuff, Eventually got this to work with a lot of help from ChatGPT as a debugging tool
## Test Data, Not actual Data I used but named the same
setwd("./Assignments/Algorithms Assignment 3/Data")
numeric_df <-read.csv("housing.csv")
numeric_df <- numeric_df[,c(1:2, 8:9)]
numeric_df <-na.omit(numeric_df)
numeric_df <- scale(numeric_df)


## Original Iterative way I found it for the project, I named it the data frame numeric_df
## because of the data set that I was using. I was mostly responsible for all the code
## On the project and in my process of cleaning the data and playing around with different techniques
## I realized to implement the ML technique I wanted to I only needed the numeric variables,
## So I took those out and just called it numeric_df beacuse I was lazy and needed an easy way to label things


set.seed(1234) # setting seed for reproducibility
wss <- (nrow(numeric_df)-1)*sum(apply(numeric_df,2,var)) # setting the starting WSS, essentially the total variance of the data set before clustering. Calculates the WSS when there is 1 cluster (whole data set is the cluster)
old_wss <- Inf # set the old WSS to be a very high value to allow us to go through the first iteration without comparison (inf - int)/inf approx 1 
for (i in 2:100) { # for number of clusters 2 through 100
  wss[i] <- sum(kmeans(numeric_df, centers=i)$withinss) #store the WSS for each number of clusters
  percentage_decrease <- ((old_wss - wss[i]) / old_wss) * 100 # calculate the percentage decrease
  if (i > 1 && !is.nan(percentage_decrease) && percentage_decrease < 5) { # if it is not the first iteration, and the percentage decrease is less than 5%
    break #exit the loop as we have found the optimal value of $k$
  }
  old_wss <- wss[i] # store the WSS from the current loop for comparison in the next iteration
}
optimal_k <- which.min(wss) # gets the index of the lowest WSS which will be the "optimal" K to choose

# Recursive version of this for loop. It is highly impractical and I am sure it can be easily broken
# it works with the data that I provided and has not been tested on any other data. 
# This is a horrible way of performing what I did iteratively using a for loop. DO NOT USE.

set.seed(1234)# setting seed or else will get different results based on kmeans randomness
find_optimal_k <- function(numeric_df, max_k = 100,
                           current_k = 2,
                           old_wss = Inf,
                           min_wss = Inf,
                           min_k = 1) {
  # Define wss locally to avoid length > 1 error, common error I had at first
  wss <- numeric(max_k + 1)  # Ensure wss has the correct length initially, and a place to store the wss
  
  if (current_k > max_k) { # Base case: Stop recursion if the current_k exceeds the maximum allowable number of clusters
    return(min_k)  # Returns the k with the minimum WSS so far if the maximum k is reached
  }
  
  # Compute WSS for the current number of centers (k)
  current_wss <- sum(kmeans(numeric_df, centers = current_k)$withinss) #This is the total WSS amongst all clusters
  wss[current_k] <- current_wss #store the current WSS
  
  # Update minimum WSS and its corresponding k
  # Need these or else the function doesn't work, returns the wrong value of k.
  # Using this in place of which.min(wss) like was used in the iterative version
 if (current_wss < min_wss) { 
    min_wss = current_wss
    min_k = current_k #store the value of the min k
  }
  
  # Calculate the percentage decrease from the old WSS if not the first run
  if (current_k > 2) {
    percentage_decrease <- ((old_wss - current_wss) / old_wss) * 100 # percentage decrease
    if (percentage_decrease <= 5) { # if that percentage decrease is 5% or less
      return(min_k)  # Return the k associated with the smallest WSS computed so far, most likely the one we just tried
    } # I DON"T TRUST THIS VERSION OF THIS LOOP, ITERATIVE VERSRION IS SO MUCH BETTER
  }
  
  old_wss <- current_wss  # Update old_wss for the next iteration
  
  # Recursive call with updated parameters
  return(find_optimal_k(numeric_df, max_k, current_k + 1, old_wss, min_wss, min_k))
}


optimal_k_recursive <- find_optimal_k(numeric_df)

# Making sure I'm getting the same answer as the iterative version
list(optimal_k_iterative = optimal_k, optimal_k_recursive = optimal_k_recursive)
