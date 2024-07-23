import pandas as pd

# Read Excel File
df = pd.read_excel("D:/Project/Data Sciences/pandas/14- Excel Report/supermarket_sales.xlsx")
 

# Select columns: 'Gender', 'Product line', 'Total'
df = df[['Gender', 'Product line', 'Total']]

# print(df.head())


# Make pivot table
pivot_table = df.pivot_table(index='Gender', columns='Product line',
                             values='Total', aggfunc='sum').round(0)

# print(pivot_table.head())

print(df.head())

# Export pivot table to Excel file
pivot_table.to_excel('D:/Project/Data Sciences/pandas/14- Excel Report/pivot_table.xlsx' , sheet_name='Report' , startrow=4)
