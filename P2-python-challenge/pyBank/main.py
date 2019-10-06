# -*- coding: UTF-8 -*-
"""PyBank Homework Solution."""

# Dependencies
import csv
import os

# Files to load and output (Remember to change these)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]
total_net = 0
pandl = []
net_monthly_avg = 0
max_net_change_date = ' '
min_net_change_date = ' '

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Read the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    next(reader)

    for row in reader:

        # Track the total
        pandl.append(int(row[1]))
        month_of_change.append(row[0])
        
        total_net = sum(pandl)
        total_months = len(month_of_change)


    # Track the net change
    #for i in range(1,len(pandl)):
    for i in range (1,len(pandl)):
        net_change_list.append((pandl[i]) - (pandl[i-1]))   

        # Calculate the greatest increase
        greatest_increase = max(net_change_list)
        max_net_change_date = str(month_of_change[net_change_list.index(max(net_change_list))])
            
        # Calculate the greatest decrease
        greatest_decrease = min(net_change_list)
        min_net_change_date = str(month_of_change[net_change_list.index(min(net_change_list))])
            
# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list)/len(net_change_list)


# Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {max_net_change_date} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {min_net_change_date} (${greatest_decrease})\n")

# Print the output (to terminal)
print(output)

# Export the results to text file
file = open(file_to_output,"w")
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${total_net}\n")
file.write(f"Average Change: ${net_monthly_avg:.2f}\n")
file.write(f"Greatest Increase in Profits: {max_net_change_date} (${greatest_increase})\n")
file.write(f"Greatest Decrease in Profits: {min_net_change_date} (${greatest_decrease})")
file.close()
