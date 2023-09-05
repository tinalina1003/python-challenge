import os
import csv

# import csv data from Resources file
pypollCSV = os.path.join("Resources", "election_data.csv")

##################################
# initialize lists and variables #
##################################

candidate = set() # create a hashset
totalVotes = 0
candidateVote = 0
listOfCandidates = []
ballot = {"Candidate": "", "Votes": ""}




##############################
# extract data from csv file #
##############################

with open(pypollCSV) as csvfile:

    # cleans up the csv
    csvreader = csv.reader(csvfile, delimiter = ",")

    csvHeader = next(csvreader)


    for row in csvreader:

        candidate.add(row[2])
    
        # counts total votes
        totalVotes += 1




print(totalVotes)







"""
import pandas as pd
from pathlib import Path

pypollCSV = Path("Resources/election_data.csv")
df = pd.read_csv(pypollCSV)

##############################
# extract data from csv file #
##############################

# extracts candidates and their corresponding votes
candidate_counts = df["Candidate"].value_counts()

totalVotes = len(df) # total votes

print(candidate_counts)
print(totalVotes)

for candidate, count in candidate_counts.items():
    percentage = (count / totalVotes) * 100
    print(f"{candidate}: {count} votes ({percentage:.3f}% of total votes)")

winner = candidate_counts.idxmax()
print(f"\nThe winner is {winner}")

print(df)
"""