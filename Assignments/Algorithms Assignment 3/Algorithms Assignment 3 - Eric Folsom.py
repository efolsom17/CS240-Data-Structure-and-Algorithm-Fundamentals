## Importing the numbers-3.txt data

with open("./Data/numbers-3.txt", "r") as nums: #opens the file
    numbers1 = [int(line.strip()) for line in nums]