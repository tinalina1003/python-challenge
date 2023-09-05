import os
import csv

# import csv data from Resources file
pypollCSV = os.path.join("Resources", "election_data.csv")

##################################
# initialize lists and variables #
##################################

#candidate = set() # create a hashset

candidateVote = 0
candidateSet= set() # create a hashset to pick out unique candidates
ballot = {"Candidate": "", "Votes": 0}
voteList = []

##############################
# extract data from csv file #
##############################

with open(pypollCSV) as csvfile:

    # cleans up the csv
    csvreader = csv.reader(csvfile, delimiter = ",")

    csvHeader = next(csvreader)

    # create a list of ballots
    electionData = list(csvreader)

    # total votes is just the length of the election data
    totalVotes = len(electionData)

    for row in range(totalVotes):
        candidateSet.add(electionData[row][2]) # add unique elements to the hashset
        candidateList = list(candidateSet) # convert set to list
        
        
        
    for i in range(len(candidateList)):
        ballot ={"Candidates": candidateList[i],
                 "Votes": 1
        }
        voteList.append(ballot)

        print(ballot)
        
print(voteList)
    








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