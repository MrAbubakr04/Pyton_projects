import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\мама\Desktop\m1_dataset.csv')
#print(df) 



df.sort_values(by='Total day charge', ascending = False).head()

#df.sort_values(by=['Churn','Total day chage'],ascending=[True,False])
df['Churn'].mean()

df[df['Churn'] == 1].mean()
