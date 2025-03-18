import pandas as pd

# Load the data
data = pd.read_csv('20250313.csv')

# Combine 'Date' and 'Time' columns into a single datetime column
data['DateTime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%Y-%m-%d %H:%M:%S')

# Calculate the absolute difference between Ctemp_set and Ctemp
data['Ctemp_diff'] = abs(data['Ctemp_set'] - data['Ctemp'])

# Filter rows where the difference is greater than 200
large_diff_periods = data[data['Ctemp_diff'] > 200]

# Group by date and count occurrences
daily_summary = large_diff_periods.groupby(large_diff_periods['DateTime'].dt.date).size()

# Print the summary
print("\nSummary of periods with large differences grouped by date:")
print(daily_summary)