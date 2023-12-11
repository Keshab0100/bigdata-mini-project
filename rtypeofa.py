#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt

# Dictionary to store cumulative count of occurrences for each description
description_count_dict = {}

for line in sys.stdin:
    # Split the input line into fields
    fields = line.strip().split('\t')

    # Extract relevant information
    description = fields[1]

    # Update the cumulative count for the current description
    description_count_dict[description] = description_count_dict.get(description, 0) + 1

# Output the results
for description, count in description_count_dict.items():
    print(f"{description}\t{count}")

# Plot the bar chart
plt.figure(figsize=(10, 6))
plt.bar(description_count_dict.keys(), description_count_dict.values())
plt.title('Cumulative Count of Occurrences by Description')
plt.xlabel('Description')
plt.ylabel('Cumulative Count')
plt.xticks(rotation=45, ha='right')
plt.ylim(0, max(description_count_dict.values()) + 5)  # Set a fixed range for the y-axis
plt.tight_layout()
plt.show()

