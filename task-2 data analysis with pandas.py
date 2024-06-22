import pandas as pd

# Load the dataset
# You can replace 'sample_data.csv' with your dataset file path
data = pd.read_csv('sample_data.csv')

# Display the first few rows of the dataset
print("First 5 rows of the dataset:")
print(data.head())

# Display basic information about the dataset
print("\nDataset Information:")
print(data.info())

# Display basic statistics of the dataset
print("\nBasic Statistics:")
print(data.describe())

# Handle missing values
# For example, filling missing values with the mean of the column
data.fillna(data.mean(), inplace=True)

# Display the number of missing values in each column
print("\nMissing values in each column after filling:")
print(data.isnull().sum())

# Perform data filtering
# For example, filter rows where a specific column 'age' is greater than 30
filtered_data = data[data['age'] > 30]
print("\nFiltered Data (age > 30):")
print(filtered_data.head())

# Perform data grouping
# For example, group by a column 'gender' and calculate the mean of each group
grouped_data = data.groupby('gender').mean()
print("\nGrouped Data (mean values by gender):")
print(grouped_data)

# Perform data aggregation
# For example, calculate the sum of a column 'income'
total_income = data['income'].sum()
print("\nTotal Income:")
print(total_income)

# Save the cleaned and analyzed data to a new CSV file
filtered_data.to_csv('cleaned_data.csv', index=False)
print("\nCleaned data saved to 'cleaned_data.csv'")
