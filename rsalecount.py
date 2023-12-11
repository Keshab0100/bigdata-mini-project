#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

# Dictionary to store cumulative count of "I" incidents for each car company
sales_count_by_company = {}

for line in sys.stdin:
    # Split the input line into fields
    fields = line.strip().split('\t')

    # Extract relevant information
    car_company = fields[1]

    # Update the cumulative count for the current car company
    sales_count_by_company[car_company] = sales_count_by_company.get(car_company, 0) + 1

# Output the results
for company, count in sales_count_by_company.items():
    print(f"{company}\t{count}")

# Plot the bar chart
plt.bar(sales_count_by_company.keys(), sales_count_by_company.values())
plt.title('Cumulative Initial Sales Count by Car Company')
plt.xlabel('Car Company')
plt.ylabel('Cumulative Initial Sales Count')
plt.show()

