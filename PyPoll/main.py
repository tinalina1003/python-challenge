import os
import csv

# import csv data from Resources file
pypollCSV = os.path.join("Resources", "election_data.csv")

##################################
# initialize lists and variables #
##################################

candidateSet= set() # create a hashset to pick out unique candidates
finalResults = []
voteList = [] # this is to store the final results
allNames = [] # this is an empty list to store EVERY SINGLE VOTED candidate
percentageList = []

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
        allNames.append(electionData[row][2]) # append ALL names people voted for into a list to count later
        
    # Count votes and calculate percentages of total votes
    for name in range(len(candidateList)):

        voteList.append(allNames.count(candidateList[name]))
        percentageList.append((voteList[name]/totalVotes) * 100)

    
    # I created dictionaries for each candidate to store name, votes, and percentage
    for candidate, count, percentage in zip(candidateList, voteList, percentageList):
        candidateDict = {
            "Candidate": candidate,
            "Votes": count,
            "Percentage of Total Votes": percentage
    }
        finalResults.append(candidateDict)

    
    winnerIndex = voteList.index(max(voteList)) # retrieve the index with the most votes and output it with the candidateList
    # Another method would be using the following line:   
    # winner = max(finalResults, key = lambda x: x['Votes']) # key = lambda specifies a small anon function which takes an argument x and returns value that will be used
    # as the comparison or sorting. It is a much faster way to retrieve the result but more confusing at my level. Like to keep this for future reference


##########
# OUTPUT #
##########

# print to terminal
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {totalVotes}")
print(f"-----------------------------")

for votes in finalResults:
    print(f"{votes['Candidate']}: {votes['Percentage of Total Votes']:.3f}% ({votes['Votes']})")

print(f"-----------------------------")
print(f"Winner: {candidateList[winnerIndex]}")
print(f"-----------------------------")

# write to analysis.txt
with open('analysis.txt', 'w') as analysisfile:
    analysisfile.write("Election Results\n") # \n next line
    analysisfile.write("----------------------------\n")
    analysisfile.write(f"Total Votes: {totalVotes}\n")
    analysisfile.write(f"-----------------------------\n")
    for votes in finalResults:
        analysisfile.write(f"{votes['Candidate']}: {votes['Percentage of Total Votes']:.3f}% ({votes['Votes']})\n")
    analysisfile.write(f"-----------------------------\n")
    analysisfile.write(f"Winner: {candidateList[winnerIndex]}\n")
    analysisfile.write(f"-----------------------------\n")

# add test line
