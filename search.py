"""
Pokemon data analysis. Using the python module numpy and pandas, this program 
analizes pokemon data in order to find what is the highest and lowest
health of a pokemon and How many of each pokemon type there is.
"""
import numpy as np
import pandas as pd 

# Read the csv file and turn it into an array
df = pd.read_csv('Pokemon.csv')
arr = df[['Name','Type 1', 'HP']].values


# Create an empty list to hold pokemon types
list_types = []

# Search through all pokemon types
for item in arr[:,1]:
    # If the pokemon type is not in
    # the list, add it to the list
    if item not in list_types:
        list_types.append(item)


# Goes through and counts each pokemon type
for item in list_types:
    
    print(f"There are {(arr[:,1] == item).sum()} {item} pokemon\n")

# Finds the highest and lowest health of a pokemon
max = (arr[:,2]).max()
min = (arr[:,2]).min()

# Prints the results
print(f"The highest health of a pokemon is {max}\n")
print(f"The lowest health of a pokemon is {min}\n")

# Prints the name of the best pokemon
print("The best pokemon is Mewtwo")


