import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data['AQI Value'] = pd.to_numeric(data['AQI Value'], errors='coerce') # Для отбора данных берем столбец AQI Value как показатель качества воздуха + заранее работаем над ошибками
plt.figure(figsize=(10, 6)) # Задаем размер

plt.hist(data['AQI Value'].dropna(), bins = 20, color='skyblue', edgecolor='black') # Отсекаем все Nan, задаем шаг в 20 bins и цвет

plt.title('AQI Value Distribution', fontsize=16)
plt.xlabel('AQI Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)

plt.show()