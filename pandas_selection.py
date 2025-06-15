import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Age': [24, 27, 22, 32, 29, 25],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'New York'],
    'Salary': [70000, 80000, 65000, 90000, 75000, 72000],
    'Experience_Years': [2, 4, 1, 7, 5, 3]
}
df = pd.DataFrame(data)
print("Original DataFrame:\n", df)
# print(df)

# The Three Pillars of Selection: [], .loc[], and .iloc[]
# These are the primary methods for selection in Pandas.

# 1. Using [] for column selection
# Selecting a single column
names = df['Name'] # When you select a single column, Pandas returns a Series.
print("Names column:\n", names)

# Selecting multiple columns
multiple_columns = df[['Name', 'Age']]  # When you select multiple columns, Pandas returns a DataFrame.
print("Multiple columns (Name and Age):\n", multiple_columns)


# selecting rows by slicing
# Selecting rows by slicing
sliced_rows = df[1:4]  # This selects rows from index 1 to 3 (4 is exclusive).
print("Sliced rows (index 1 to 3):\n", sliced_rows)

# Boolean indexing
# Selecting rows based on a condition 
condition = df['Age'] > 25  # Condition to filter rows where Age is greater than 25
filtered_rows = df[condition]  # This returns rows where the condition is True.
print("Filtered rows (Age > 25):\n", filtered_rows)

# Selecting rows based on multiple conditions
condition_multiple = (df['Age'] > 25) & (df['City'] == 'Houston')  # Multiple conditions  
print("Filtered rows (Age > 25 and City is New York):\n", df[condition_multiple])





# 2. Using .loc[] for label-based selection
# Selecting rows and columns by labels; labels are the index and column names.
# Selecting a single row by label
single_row = df.loc[2]  # This selects the row with index label 2.
print("Single row (index 2):\n", single_row)

# sselectin multiple rows by index labels
specific_rows = df.loc[[0, 2, 4]]  # This selects rows with index labels 0, 2, and 4.
print("Specific rows (index 0, 2, and 4):\n", specific_rows)

# Selecting multiple rows by labels
multiple_rows = df.loc[1:3]  # This selects rows from index 1 to 3 (inclusive).
print("Multiple rows (index 1 to 3):\n", multiple_rows)


# selecting columns by labels
# Selecting a single column by label
single_column = df.loc[:, 'City']  # This selects the 'City' column for all rows.
print("Single column (City):\n", single_column)

# Selecting specific rows and columns by labels
specific_selection = df.loc[1:3, ['Name', 'Salary']]  # Selecting rows 1 to 3 and columns 'Name' and 'Salary'.
print("Specific selection (rows 1 to 3 and columns Name and Salary):\n", specific_selection)

# Selecting both rows and columns simultaneously
# Selecting both rows and columns simultaneously
both_selection = df.loc[[1,3,4], ['Name', 'Age', 'City']]  # Selecting specific rows 1, 3, 4 and columns 'Name', 'Age', and 'City'.
print("Both selection ( specific rows 1, 3, 4 and columns Name, Age, City):\n", both_selection)

# Selecting rows based on a condition using .loc[]
condition_loc = df.loc[df['Age'] > 25, ['Name', 'City']]  # Selecting rows where Age > 25 and columns 'Name' and 'City'.
print("Rows where Age > 25 with columns Name and City:\n", condition_loc)

# Selecting a specific cell by label
specific_cell = df.loc[2, 'City']  # This selects the City of the row with index label 2.
print("Specific cell (City of index 2):", specific_cell)
# Selecting a range of rows and columns by labels
# Selecting a range of rows and columns by labels

range_selection = df.loc[1:4, ['Name', 'Age', 'City']]  # Selecting rows 1 to 4 and columns 'Name', 'Age', and 'City'.
print("Range selection (rows 1 to 4 and columns Name, Age, City):\n", range_selection)
# Selecting rows based on a condition using .loc[]
condition_loc_multiple = df.loc[(df['Age'] > 25) & (df['City'] == 'New York'), ['Name', 'Salary']]  # Selecting rows where Age > 25 and City is New York.
print("Rows where Age > 25 and City is New York with columns Name and Salary:\n", condition_loc_multiple)

# Selecting a specific cell by label
specific_cell_loc = df.loc[3, 'Salary']  # This selects the Salary of the row with index label 3.
print("Specific cell (Salary of index 3):", specific_cell_loc)

# slicing both rows and columns
sliced_both = df.loc[1:4, 'Name':'City']  # This selects rows 1 to 4 and columns from 'Name' to 'City'.
print("Sliced both (rows 1 to 4 and columns Name to City):\n", sliced_both)

# Selecting rows based on a condition using .loc[]
condition_loc_sliced = df.loc[df['Age'] > 25, 'Name':'City']  # Selecting rows where Age > 25 and columns from 'Name' to 'City'.
print("Rows where Age > 25 with columns Name to City:\n", condition_loc_sliced)





# 3. Using .iloc[] for position-based selection ( Integer-location based Selection with .iloc[] )
# Selecting rows and columns by integer positions; positions are the row and column indices.
# Selecting a single row by position
single_row_iloc = df.iloc[2]  # This selects the row at position 2 ( Series ). 
print("Single row (position 2):\n", single_row_iloc)

# Selecting multiple rows by positions
multiple_rows_iloc = df.iloc[[0, 2, 4]]  # This selects rows at positions 0, 2, and 4 ( DataFrame ).
print("Multiple rows (positions 0, 2, and 4):\n", multiple_rows_iloc)

# Selecting a range of rows by positions
range_rows_iloc = df.iloc[1:4]  # This selects rows from position 1 to 3 (4 is exclusive).
print("Range of rows (positions 1 to 3):\n", range_rows_iloc)

# Selecting a single column by position
single_column_iloc = df.iloc[:, 2]  # This selects the column at position 2 ( 'City' ).
print("Single column (position 2):\n", single_column_iloc)

# Selecting specific rows and columns by positions
specific_selection_iloc = df.iloc[1:4, [0, 3]]  # Selecting rows 1 to 3 and columns at positions 0 and 3 ( 'Name' and 'Salary' ).
print("Specific selection (rows 1 to 3 and columns at positions 0 and 3):\n", specific_selection_iloc)

# Selecting both rows and columns simultaneously by positions
both_selection_iloc = df.iloc[[1, 3, 4], [0, 1, 2]]  # Selecting specific rows 1, 3, 4 and columns at positions 0, 1, and 2 ( 'Name', 'Age', 'City' ).
print("Both selection ( specific rows 1, 3, 4 and columns at positions 0, 1, 2):\n", both_selection_iloc)

# Selecting rows based on a condition using .iloc[]
condition_iloc = df.iloc[df['Age'] > 25, [0, 2]]  # Selecting rows where Age > 25 and columns at positions 0 and 2 ( 'Name' and 'City' ).
print("Rows where Age > 25 with columns at positions 0 and 2:\n", condition_iloc)

# Selecting a specific cell by position
specific_cell_iloc = df.iloc[2, 2]  # This selects the City of the row at position 2.
print("Specific cell (City of position 2):", specific_cell_iloc)

# Selecting a range of rows and columns by positions
range_selection_iloc = df.iloc[1:4, [0, 1, 2]]  # Selecting rows 1 to 3 and columns at positions 0, 1, and 2 ( 'Name', 'Age', 'City' ).
print("Range selection (rows 1 to 3 and columns at positions 0, 1, 2):\n", range_selection_iloc)

# Selecting rows based on a condition using .iloc[]
condition_iloc_multiple = df.iloc[(df['Age'] > 25) & (df['City'] == 'New York'), [0, 3]]  # Selecting rows where Age > 25 and City is New York, and columns at positions 0 and 3 ( 'Name' and 'Salary' ).
print("Rows where Age > 25 and City is New York with columns at positions 0 and 3:\n", condition_iloc_multiple)

# Selecting a specific cell by position
specific_cell_iloc_pos = df.iloc[3, 3]  # This selects the Salary of the row at position 3.
print("Specific cell (Salary of position 3):", specific_cell_iloc_pos)

# Slicing both rows and columns by positions
sliced_both_iloc = df.iloc[1:4, 0:3]  # This selects rows 1 to 3 and columns from position 0 to 2 ( 'Name', 'Age', 'City' ).
print("Sliced both (rows 1 to 3 and columns from position 0 to 2):\n", sliced_both_iloc)

# Selecting rows based on a condition using .iloc[]
condition_iloc_sliced = df.iloc[df['Age'] > 25, 0:3]  # Selecting rows where Age > 25 and columns from position 0 to 2 ( 'Name', 'Age', 'City' ).
print("Rows where Age > 25 with columns from position 0 to 2:\n", condition_iloc_sliced)

# Summary of Selection Methods
# Summary of Selection Methods
print("\nSummary of Selection Methods:")
print("1. []: Used for selecting columns and rows by slicing or boolean indexing.")
print("2. .loc[]: Used for label-based selection of rows and columns, allowing for more complex conditions.")
print("3. .iloc[]: Used for position-based selection of rows and columns, allowing for integer indexing.")
# Conclusion
print("\nConclusion:")
print("Pandas provides powerful selection methods to access and manipulate data in DataFrames. Understanding the differences between [], .loc[], and .iloc[] is crucial for effective data analysis.")
# The code demonstrates the three primary methods of selection in Pandas: [], .loc[], and .iloc[].
# Each method has its own use cases and advantages, allowing for flexible data manipulation and analysis.


