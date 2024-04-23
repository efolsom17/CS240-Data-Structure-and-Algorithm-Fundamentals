#testing stuff
numeric_df <-read.csv("C:/Users/Eric Folsom/Desktop/School work/CS240-Data-Structure-and-Algorithm-Fundamentals/Assignments/Algorithms Assignment 3/Data/housing.csv")
numeric_df <- numeric_df[,c(1:2, 8:9)]
numeric_df <-na.omit(numeric_df)
numeric_df <- scale(numeric_df)


set.seed(1234) # setting seed for reproducibility
wss <- (nrow(numeric_df)-1)*sum(apply(numeric_df,2,var)) # setting the starting WSS, essentially the total variance of the data set before clustering. Calculates the WSS when there is 1 cluster (whole data set is the cluster)
old_wss <- Inf # set the old WSS to be a very high value to allow us to go through the first iteration without comparison (inf - int)/inf approx 1 
for (i in 2:100) { # for number of clusters 2 through 100
  wss[i] <- sum(kmeans(numeric_df, centers=i)$withinss) #store the WSS for each number of clusters
  percentage_decrease <- ((old_wss - wss[i]) / old_wss) * 100 # calculate the percentage decrease
  print(paste("Current k: ", i, "WSS:", wss[i], "Percentage decrease:", percentage_decrease))
  if (i > 1 && !is.nan(percentage_decrease) && percentage_decrease < 5) { # if it is not the first iteration, and the percentage decrease is less than 5%
    break #exit the loop as we have found the optimal value of $k$
  }
  old_wss <- wss[i] # store the WSS from the current loop for comparison in the next iteration
}
optimal_k <- which.min(wss) # gets the index of the lowest WSS which will be the "optimal" K to choose




optimal_k_iterative <- which.min(wss)


set.seed(1234)
find_optimal_k <- function(numeric_df, max_k = 100, current_k = 2, old_wss = Inf, min_wss = Inf, min_k = 1) {
  # Define wss locally to avoid length > 1 error in condition checks
  wss <- numeric(max_k + 1)  # Ensure wss has the correct length initially
  
  if (current_k > max_k) {
    return(min_k)  # Returns the k with the minimum WSS so far if the maximum k is reached
  }
  
  # Compute WSS for the current number of centers (k)
  current_wss <- sum(kmeans(numeric_df, centers = current_k)$withinss)
  wss[current_k] <- current_wss
  
  # Update minimum WSS and its corresponding k
  if (current_wss < min_wss) {
    min_wss = current_wss
    min_k = current_k
  }
  
  # Calculate the percentage decrease from the old WSS if not the first run
  if (current_k > 2) {
    percentage_decrease <- 100 * (old_wss - current_wss) / old_wss
    
    if (percentage_decrease <= 5) {
      return(min_k)  # Return the k associated with the smallest WSS computed so far
    }
  }
  
  old_wss <- current_wss  # Update old_wss for the next iteration
  
  # Recursive call with updated parameters
  return(find_optimal_k(numeric_df, max_k, current_k + 1, old_wss, min_wss, min_k))
}
# Initialize and run the recursive function
optimal_k_recursive <- find_optimal_k(numeric_df)


# Display results
list(optimal_k_iterative = optimal_k_iterative, optimal_k_recursive = optimal_k_recursive)
