# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path("PyRamen/menu_data.csv')
sales_filepath = Path("PyRamen/sales_data.csv")

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list

with open(menu_filepath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
                     
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # Print the header
    print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        # Print the row
        print(row)



# @TODO: Read in the sales data into the sales list
with open(sales_filepath, 'r') as file:
    csvreader = csv.reader(csvfile, delimiter=',')

      # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # Print the header
    print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        # Print the row
        print(row)                   



# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object

with open(sales_filepath, 'r') as file:
    csvwriter = csv.writer(csvfile, delimiter=",")
    # Write the header as the first row
    csvwriter.writerow('header')
    
    for name in sales:
        csvwriter.writerow(
            [
                name,
                sales[name]["Line_Item_ID"],
                sales[name]["Date"],
                sales[name]["Credit_Card_Number"]
                sales[name]["Quantity"]
                sales[name]["Menu_Item"]
                
            ]
        )



    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables


    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit








    # @TODO: For every row in our sales data, loop over the menu records to determine a match


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables




        # @TODO: Calculate profit of each item in the menu data


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item


            # @TODO: Print out matching menu data






            # @TODO: Cumulatively add up the metrics for each item key





        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match



    # @TODO: Increment the row counter by 1


# @TODO: Print total number of records in sales data




# @TODO: Write out report to a text file (won't appear on the command line output)