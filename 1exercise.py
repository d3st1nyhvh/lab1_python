import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 

data['AQI Value'] = pd.to_numeric(data['AQI Value'], errors='coerce') # Для отбора данных берем столбец AQI Value как показатель качества воздуха
plt.figure(figsize=(12, 6))

plt.boxplot(data['AQI Value'].dropna(), vert=False, patch_artist=True,
            boxprops=dict(facecolor='lightblue'), whiskerprops=dict(color='blue'), medianprops=dict(color='red')) # Построение "ящика с усами"

plt.title('AQI Value Boxplot', fontsize=16)
plt.xlabel('AQI Value', fontsize=12)
plt.ylabel('Boxplot of AQI Value', fontsize=16)

plt.show()