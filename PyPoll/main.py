# Import modules
import os
import csv

# Open up empty lists for calculations
long_candidate = []
short_candidate = []

# Open file
csvpath = os.path.join("Resources", "election_data.csv")
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip over the header/1st row
    next(csvreader)

    # Move the candidates into their own list
    for row in csvreader:
        long_candidate.append(row[2])

# Get total number of votes
total_votes = len(long_candidate)

# Go down each row in the full list of candidates
for row in long_candidate:
    # Populate unique names in the short candidate list
    if row not in short_candidate:
        short_candidate.append(row)

# Tally up the number of votes each candidate received
khan_total = long_candidate.count(short_candidate[0])
correy_total = long_candidate.count(short_candidate[1])
li_total = long_candidate.count(short_candidate[2])
otooley_total = long_candidate.count(short_candidate[3])

# Find percentage of votes for each candidate
# Format to 3 decimal places
khan_percent = format((100 * khan_total / total_votes), '.3f')
correy_percent = format((100 * correy_total / total_votes), '.3f')
li_percent = format((100 * li_total / total_votes), '.3f')
otooley_percent = format((100 * otooley_total / total_votes), '.3f')

# Count # of times candidates list (short) appears in full list (long)
# The max count received the most votes (winner)
winner = max(short_candidate, key = long_candidate.count)

# Print summary table header
print(f'''"Election Results"
----------------------------
Total Votes: {total_votes}
----------------------------
{short_candidate[0]}: {khan_percent}% ({khan_total})
{short_candidate[1]}: {correy_percent}% ({correy_total})
{short_candidate[2]}: {li_percent}% ({li_total})
{short_candidate[3]}: {otooley_percent}% ({otooley_total})
----------------------------
Winner: {winner}
----------------------------''')

# Open txt file
txtpath = os.path.join("analysis", "poll_txt.txt")
poll_txt = open(txtpath, "w")

# Print results in the text file
poll_txt.write(f'''Election Results
----------------------------
Total Votes: {total_votes}
----------------------------
{short_candidate[0]}: {khan_percent}% ({khan_total})
{short_candidate[1]}: {correy_percent}% ({correy_total})
{short_candidate[2]}: {li_percent}% ({li_total})
{short_candidate[3]}: {otooley_percent}% ({otooley_total})
----------------------------
Winner: {winner}
----------------------------''')