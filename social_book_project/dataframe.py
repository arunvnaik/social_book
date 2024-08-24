import pandas as pd

# Create a list of lists
data = [
    [1, 20, 300],
    [4, 50, 600],
    [7, 80, 900],
    [10, 110, 1200],
    [13, 140, 1500],
    [16, 170, 1800],
    [19, 200, 2100],
    [22, 230, 2400],
    [25, 260, 2700],
    [28, 290, 3000]
]

# Create a DataFrame
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

print(df)


import pandas as pd

# Create a dictionary
data = {
    'A': [1, 4, 7, 10, 13, 16, 19, 22, 25, 28],
    'B': [20, 50, 80, 110, 140, 170, 200, 230, 260, 290],
    'C': [300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700, 3000]
}

# Create a DataFrame
df = pd.DataFrame(data)

print(df)


# Filter rows where column 'B' > 100
filtered_df = df[df['B'] > 100]

print(filtered_df)

# Filter based on conditions on two columns
filtered_df_two_columns = df[(df['A'] > 10) & (df['C'] < 2000)]

print(filtered_df_two_columns)

# Replace values in column 'C' where values are greater than 2000
df['C'] = df['C'].apply(lambda x: 999 if x > 2000 else x) 

print(df)

import numpy as np

# Create a second DataFrame with random data
data2 = np.random.randint(1, 100, size=(10, 3))

# Creating DataFrame from random data
df2 = pd.DataFrame(data2, columns=['A', 'B', 'C'])

print("First DataFrame:")
print(df)

print("\nSecond DataFrame:")
print(df2)

# Append df2 to df
appended_df = df._append(df2, ignore_index=True)

print("\nAppended DataFrame:")
print(appended_df) 

