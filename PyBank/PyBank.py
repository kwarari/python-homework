"""PyBabnk Assignment


# Import the pathlib and csv library
from pathlib import Path
import csv

# Set the path using Pathlib
csvpath = Path('../PyBank/budget_data.csv')

# Initialize list of records
records = []
    
# Open the csv file as an object
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is no header)
    header = next(csvreader)
    print(header)
    
    # Append the column 'Average' to the header
    header.append("Average")
    # Append the header to the list of records
    records.append(header)
    
