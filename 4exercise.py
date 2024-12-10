import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data = pd.read_csv('Airpollution.csv') 
data_number = data.select_dtypes(include = [np.number]) # выбор только числовых данных
data_log = data_number.apply(lambda x : np.log(x+1)) # Логарифмирование данных
print (data_log)