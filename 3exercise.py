import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data = pd.read_csv('Airpollution.csv') 
data_number = data.select_dtypes(np.number) # выбор только числовых данных
print(data_number.head) 