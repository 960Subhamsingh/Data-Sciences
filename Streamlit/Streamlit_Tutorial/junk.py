import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Set the random seed for reproducibility
np.random.seed(42)

# Define the number of samples
num_samples = 800*4

# Generate random dates between start_date and end_date
start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = (end_date - start_date).days
dates_ordered = [start_date + timedelta(days=np.random.randint(date_range))
                 for _ in range(num_samples)]

# Sort the dates to simulate the chronological order
dates_ordered.sort()

# Generate other fields based on the 'dates_ordered'
dates_shipped = [date + timedelta(days=np.random.randint(1, 5))
                 for date in dates_ordered]
num_days_since_shipped = [(datetime(2024, 2, 24) - ds).days for ds in dates_shipped]
usernames = [f'@User{np.random.randint(1, 1000)}' for _ in range(num_samples)]
items = ['Item x', 'Item y', 'Item z', 'Item g', 'Item h', 'Item c']
orders = [f'{np.random.choice(items)} - {np.random.randint(1, 101)} units' for _ in range(num_samples)]
addresses = ['Name Address Zipcode City' for _ in range(num_samples)]
revenue = np.random.uniform(100, 1000, num_samples).round(2)
expenses = np.random.uniform(10, 100, num_samples).round(2)
profit = revenue - expenses
revenue_accumulated = np.cumsum(revenue).round(2)
profit_accumulated = np.cumsum(profit).round(2)
expenses_accumulated = np.cumsum(expenses).round(2)

# Create a DataFrame
junk_data = pd.DataFrame({
    'Date ordered': dates_ordered,
    'Date shipped': dates_shipped,
    'Num days since shipped': num_days_since_shipped,
    'USERNAME': usernames,
    'Order': orders,
    'Delivery address': addresses,
    'Revenue': revenue,
    'Expenses': expenses,
    'Profit': profit,
    'Revenue ': revenue_accumulated,
    'Profit ': profit_accumulated,
    'Expenses': expenses_accumulated
})

# Save the DataFrame to a CSV file
# Save the DataFrame to a tab-delimited file
junk_data.to_csv('junk_sales_data.tsv', sep='\t', index=False)

print("Junk data generated and saved to 'junk_sales_data.csv'.")

