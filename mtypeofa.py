#!/usr/bin/env python

import sys

# Input format: [Transaction Type],[Vehicle Identifier],[Description],...

for line in sys.stdin:
    # Split the input line into fields
    fields = line.strip().split(',')

    # Extract relevant information
    transaction_type = fields[1]
    vehicle_identifier = fields[2]
    description = fields[7]

    # Emit the vehicle identifier, description, and transaction type for accidents
    if transaction_type == 'A':
        print(f"{vehicle_identifier}\t{description}\t{transaction_type}")

