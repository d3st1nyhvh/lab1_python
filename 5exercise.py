import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data = pd.read_csv('Airpollution.csv') 
data_number = data.select_dtypes(include = [np.number]) # выбор только числовых данных
data_log = data_number.apply(lambda x : np.log(x+1))

for values in data_log.columns:
    plt.figure(figsize=(12, 6))
    
    #Диаграмма размаха
    plt.subplot(1, 2, 1)
    data_log.boxplot(column=values)
    plt.title(f'Boxplot of {values}')
    
    #Гистограмма
    plt.subplot(1, 2, 2)
    plt.hist(data_log[values].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.tight_layout()
    plt.show()