"""
Pokemon data analysis. Using the python module numpy, this program 
analizes pokemon data in order to answer two questions. What is the max, 
min, and average health of each type of pokemon? and How many of each 
pokemon type is there?
"""
import numpy as np
import pandas as pd 

array = pd.read_csv('Pokemon.csv', header=0).values

print(array)

