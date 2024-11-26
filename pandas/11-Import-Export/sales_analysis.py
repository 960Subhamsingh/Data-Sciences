import pandas as pd

data = pd.read_csv("D:/Project/Data Sciences/pandas/11-Import-Export/data/Details.csv")

##print(data.groupby('Sub_Category').agg({'Profit':['mean','max','count','sum'],'Quantity':['mean','max','count','sum']}))

##print(data.groupby(['Category', 'Sub_Category']).agg({'Profit':['mean','max','count','sum']}))


print(data.groupby(['Category', 'Sub_Category']).describe())
