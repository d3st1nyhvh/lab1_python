import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data = pd.read_csv('Airpollution.csv') 

print ("\n\nMissing value count:\n\n",data.isna().sum())  # Задание 10
print ("\n\nDuplicated value count:\n\n",data.duplicated()) # Задание 11
new_data = data.drop_duplicates()

print ("\n\nAfter drop duplicates:\n") # Задание 11
print (new_data.duplicated())