#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt

master_info = {}

def flush():
    # Lists to store data for visualization
    years = []
    accident_counts = []

    for key in master_info.keys():
        make = master_info[key]["make"]
        year = master_info[key]["year"]
        accident_count = master_info[key]["accident_count"]

        # Append data for visualization
        years.append(year)
        accident_counts.append(accident_count)

        # Prints make, year, and accident_count
        print(f'{make}\t{year}\t{accident_count}')

    # Plot the bar chart
    plt.bar(years, accident_counts)
    plt.title('Number of Accidents by Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Accidents')
    plt.show()

for line in sys.stdin:
    line = line.strip()
    vin_number, values = line.split('\t')
    
    # List comprehension to remove unnecessary characters and extract desired values.
    values_list = [val.replace("'", "").replace("(", "").replace(")", "").replace(" ", "") for val in values.split(",")]
    incident_type = values_list[0]
    vehicle_make = values_list[1]
    vehicle_year = values_list[2]

    # check if vin is in dict
    if vin_number not in master_info:
        master_info[vin_number] = {"make": None, "year": None, "accident_count": 0}

    # grab vehicle make and year from master_info, only where incident type == I
    if incident_type == "I":
        master_info[vin_number]["make"] = vehicle_make
        master_info[vin_number]["year"] = vehicle_year

    # increment count for each incident type == A
    if incident_type == "A":
        master_info[vin_number]["accident_count"] += 1

flush()

