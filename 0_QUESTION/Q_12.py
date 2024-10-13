"""
Return the details of employees whose Salaries are higher
 than their department's average salary
"""

import pandas as pd

employee_info=[
    [1, 'mahendra', 3, 'Data Analytics', 50000],
    [2, 'sai', 4, 'IT', 60000],
    [3, 'madhav', 1, 'Software', 75000],
    [4, 'uma', 2, 'Data Analytics', 85000],
    [5, 'obul', 3, 'IT', 96000],
    [6, 'sam',2, 'IT', 55000],[7, 'umesh',4, 'Data Analytics',70000],
    [8,'ram',3,'Software',30000]
]

data = pd.DataFrame(employee_info, columns=['emp_id', 'emp_name','mag_id', 'department','salary'] )


data_avg=data.groupby('department')['salary'].mean().reset_index(name='department_avg_sales')

ddat= data.merge(data_avg,on = 'department')

dt = ddat[ddat['salary']>ddat['department_avg_sales']]

print(dt.head())