#!/usr/bin/env python

import sys

# Input format: [Transaction Type],[Vehicle Identifier],[Car Company],...

for line in sys.stdin:
    # Split the input line into fields
    fields = line.strip().split(',')

    # Extract relevant information
    transaction_type = fields[1]
    vehicle_identifier = fields[2]
    car_company = fields[3]

    # Emit the vehicle identifier, car company, and transaction type
    if transaction_type == 'I':
    	print(f"{vehicle_identifier}\t{car_company}\t{transaction_type}")

