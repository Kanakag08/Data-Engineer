# write to csv file
import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emily'],
        'Age': [25, 30, 22, 35, 28],
        'Salary': [50000, 60000, 45000, 70000, 55000]}
df = pd.DataFrame(data)

# Write DataFrame to CSV
df.to_csv('output.csv', index=False)
