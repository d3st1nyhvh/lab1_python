import pandas as pd 
import matplotlib.pyplot as plt  
import numpy as np  

data = pd.read_csv('Airpollution.csv')
print ("\n\nBase info:\n") 
data.info() # Задание 6
print ("\n\nType info:\n",data.dtypes) # Задание 7
print ("\n\nLen info:\n",data.shape) # Задание 8
print ("\n\nColums info:\n",data.columns.values) # Задание 9