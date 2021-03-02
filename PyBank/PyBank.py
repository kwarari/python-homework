
"""PyBabnk Assignment

Using Pandas

# Import the pathlib and csv library
from pathlib import Path
import csv
import pandas as pd

# Initialize list of records
records = []

# Set the path using Pathlib
csvpath = Path('../PyBank/budget_data.csv')

# Read in CSV as DataFrame
data_csv = pd.read_csv(csvpath)
data_csv.head()

#total number of months
data_csv["Profit/Losses"].count()
print(f"Total Months: {data_csv['Profit/Losses'].count()}")

#The average of the changes in Profit/Losses over the entire period.
data_csv["Profit/Losses"].mean()

data_csv['pnl_changes']=data_csv["Profit/Losses"]- data_csv["Profit/Losses"].shift()
data_csv

Mean_PL= data_csv["pnl_changes"].mean()
print(f"Average Profit/Losses: {Mean_PL}")


#The greatest increase in profits (date and amount) over the entire period.
data_csv["pnl_changes"].max()      
data_csv.loc[data_csv["pnl_changes"] == data_csv["pnl_changes"].max(),'Date']

#The greatest decrease in losses (date and amount) over the entire period.
data_csv["pnl_changes"].min()
data_csv.loc[data_csv["pnl_changes"] == data_csv["pnl_changes"].min(),'Date']


  print("Financial Analysis")
print("----------------------")
print(f"Total Months: {Total_months}")
print(f"Total Profit/Loss: {data_csv['Profit/Losses'].sum()}")
print(f"Average Profit/Losses: {Mean_PL}")
print(f"Greatest Increase in Profits: Feb-2012 ${1926159.0}")
print(f"Greatest Decrease in Profits: Sep-2013 $({-2196167.0})")









"""PyBabnk Assignment
#(Python)
#(although unable to execute code successfully)

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
for row in csvreader:
    print(row)
    line_num += 1
    profitloss.append(int(row[1]))
    profitloss_sum += int(row[1])
    profitloss_dates.append(row[0])
    
     # Append the column 'Average' to the header
    header.append("Average")
    # Append the header to the list of records
    records.append(header)
    
#The average of the changes in Profit/Losses over the entire period.
    
    profitloss_change = []

for i in range(1, len(profitloss)):
    x = profitloss[i] - profitloss[i - 1]
    profitloss_change.append(int(x))
    
for i in range(0, len(profitloss_change)):
    sum += profitloss_change[i]
    average_change_profitloss = round((sum / (len(profitloss_change))), 2)
    
for profloss in profitloss:
    
    if min_pl == 0:
        max_pl == profitloss
        min_pl == profitloss
    if profitloss > max_pl:
        max_pl = profitloss
    elif profitloss < min_pl:
        min_pl = profitloss
        
#The greatest increase in profits (date and amount) over the entire period. #The greatest decrease in losses (date and amount) over the entire period.

max_pl_index = profitloss.index(max_pl)
min_pl_index = profitloss.index(min_pl)

max_pl_date = profitloss_dates[max_pl_index]
min_pl_date = profitloss_dates[min_pl_index]

print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {line_num} ")
print(f"Total: ${profitloss_sum}")
print(f"Average Change: ${average_change_profitloss}")
print(f"Greatest Increase in Profits: ${max_pl} on {max_pl_date}")
print(f"Greatest Decrease in Profits: ${min_pl} on {min_pl_date}")

#Output

output_path = Path('Financial_Analysis.txt')

with open(output_path, 'w') as file:
    file.write("Financial Analysis")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {Total_months}")
    file.write(f"Total Profit/Loss: {data_csv['Profit/Losses'].sum()}")
    file.write(f"Average Profit/Losses: {Mean_PL}")
    file.write(f"Greatest Increase in Profits: Feb-2012 ${1926159.0}")
    file.write(f"Greatest Decrease in Profits: Sep-2013 $({-2196167.0})")
    
    
    
