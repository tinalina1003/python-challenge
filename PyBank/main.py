import os
import csv

# import csv data from Resources file
pybankCSV = os.path.join("Resources", "budget_data.csv")

# create empty lists
date = [] # create a list of months to zip later
amount = [] # creat a list of profits/losses to zip later
changeList = [] # create a list to store differences between each month
monthCount = 0 # month counter
total = 0 # net Total amount of Profit/ Losses over the entire period
sumOfChanges = 0 # sum for the changes to average out
greatestInc = 0 # greatest increase in profits over the entire period
greatestDec = 0 # greatest decrease in profits over the entire period
highestDate = "" # place holder for date
lowestDate = "" # place holder for date

# extract data from csv file
with open(pybankCSV) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Skips the header (there is a header in this case)
    csv_header = next(csvreader)

    previousRevenue = 0

    for row in csvreader:
        
        currentRevenue = float(row[1])
        total += currentRevenue # total revenue
        monthCount += 1
        changeRevenue = currentRevenue - previousRevenue
        date.append(row[0])
        changeList.append(changeRevenue) # I need to keep this date, revenue pair so I can find out the highest/lowest increase in profits
        previousRevenue = currentRevenue

        # update greatest increase in profits
        
        #if changeRevenue > greatestInc:
        #    greatestInc = changeRevenue
        

    # slice the first element of the average revenue list because we do not cannot assume we start from 0 prior to the first date
    date = date[1:]
    changeList = changeList[1:]

dateRevPair = zip(date, changeList)

# find the greatest increase and decrease in profits with date/amount pair over the entire period
for pairs in dateRevPair:

    if pairs[1] > greatestInc:

        greatestInc = pairs[1]
        highestDate = pairs[0]

    if pairs[1] < greatestDec:

        greatestDec = pairs[1]
        lowestDate = pairs[0]
    

print(highestDate, greatestInc) # greatest increase in profits pair
print(lowestDate, greatestDec)







