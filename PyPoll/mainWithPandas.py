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