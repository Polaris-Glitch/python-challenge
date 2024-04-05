# pypoll instruction.py

#import os and establish Path
import os
import csv

csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

#read in csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

# create lists for each column in csv file
    Ballot_ID = []
    County = []
    Candidate = []

    for row in csvreader:
       Ballot_ID.append(row[0])
       County.append(row[1])
       Candidate.append(row[2])

# establish variables to calculate votes and percentages
    c_1 = Candidate.count('Charles Casper Stockham')
    c_2 = Candidate.count('Diana DeGette')
    c_3 = Candidate.count('Raymon Anthony Doane')
    total_votes = len(Ballot_ID)

#calculate and print results
print("Election Results")
print("------------------------------------------------------")
print("Total Votes: " + str(len(Ballot_ID)))
print("------------------------------------------------------")
print("Charles Casper Stockham: " + str(round((c_1/total_votes)*100, 3)) + "% (" + str(c_1) + ") ")
print("Diana DeGette: " + str(round((c_2/total_votes)*100, 3)) + "% (" + str(c_2) + ") ")
print("Raymon Anthony Doane: " + str(round((c_3/total_votes)*100, 3)) + "% (" + str(c_3) + ")")     

print("------------------------------------------------------")
print("Winner: Diana GeGette")

print("------------------------------------------------------")