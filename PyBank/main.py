# Import modules
import os
import csv

# Open up empty lists for calculations
date = []
pl = []
pl_change = []

# Open file
csvpath = os.path.join("Resources", "budget_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip over header/1st row
    next(csvreader)

    # Assign dates and profit/loss into their own lists
    for row in csvreader:
        date.append(row[0])
        pl.append(row[1])

# Count months
date_count = len(list(date))

# Convert pl into integers (currently strings)
int_pl = [int(x) for x in pl]

# Sum profit/loss list
sum_pl = sum(int_pl)

# Calc month over month change
# Subtract profit/loss from month above
# Populate results in a new list "pl_change"
for row in range(1, len(int_pl)):
    delta = int_pl[row] - int_pl[row - 1]
    pl_change.append(delta)

# Average change = sum / count
# Round to to decimal places
sum_chg = sum(pl_change)
len_pl = len(pl_change)
avg_change = round((sum_chg/len_pl), 2)

# Define the max and min profit/loss change
max_change = max(pl_change)
min_change = min(pl_change)

# Find the row # for the max & min to index/match with the date
max_index = pl_change.index(max_change)
min_index = pl_change.index(min_change)

# Match the corresponding dates to the index
# Need to go down a row (+1): change table starts from the 2nd voter
max_date = date[max_index + 1]
min_date = date[min_index + 1]

# Print results
print(f'''Financial Analysis
----------------------------
Total Months: {date_count}
Total: ${sum_pl}
Average Change: ${avg_change}
Greatest Increase in Profits: {max_date} (${max_change})
Greatest Decrease in Profits: {min_date} (${min_change})''')

# Open txt file
txtpath = os.path.join("analysis", "bank_txt.txt")
bank_txt = open(txtpath, "w")

# Print results in the text file
bank_txt.write(f'''Financial Analysis
----------------------------
Total Months: {date_count}
Total: ${sum_pl}
Average Change: ${avg_change}
Greatest Increase in Profits: {max_date} ($ {max_change})
Greatest Decrease in Profits: {min_date} ($ {min_change})''')