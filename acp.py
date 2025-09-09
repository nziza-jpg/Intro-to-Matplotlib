import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Company Sales Data.csv')

plt.plot(df['month_number'], df['total_profit'], 
         linestyle='dotted',        
         marker='o',
         mec='black',         
         color='r',
         linewidth=3)          

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Profit')
plt.title('Month-wise Profit of the Company')
plt.legend()
plt.show()

x = np.arange(len(df['month_number']))
plt.bar(x, df['facecream'], label='Face Cream', color='skyblue')
plt.bar(x, df['facewash'], label='Face Wash', color='orange')
plt.xlabel('Month')
plt.ylabel('Sales Units')
plt.title('Monthly Sales: Face Cream vs Face Wash')
plt.xticks(x, df['month_number'])
plt.legend()
plt.show()