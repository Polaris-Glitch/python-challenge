# pybank instruction

#read in csv file and format ourtput

import os
import csv
from statistics import mean

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
   
    Date = []
    Value = []

    for row in csvreader:
        Date.append(row[0])
        Value.append(int(row[1]))  # Convert value to int for calculations

    Change = []
    
    for i in range(1, len(Value)):
        # Calculate the change by subtracting the previous value from the current one
        change = Value[i] - Value[i - 1]
        Change.append(change) 
    Change.insert(0,0)


print("Financial Analysis")
print("--------------------------------------------------------")

# Total number of months
print("Total Months: " + str(len(Date)))

# Net total of "profit/losses"
print("Total: $" + str(sum(Value)))

# Average change
average_change = mean(Change)
print("Average Change: $" + str(round(average_change, 2)))

# Greatest increase in profit (date and amount)
max_change_index = Change.index(max(Change))
print("Greatest Increase in Profits:", Date[max_change_index], "($" + str(max(Change)) + ")")

# Greatest decrease in profit (date and amount)
min_change_index = Change.index(min(Change))
print("Greatest Decrease in Profits:", Date[min_change_index], "($" + str(min(Change)) + ")")
