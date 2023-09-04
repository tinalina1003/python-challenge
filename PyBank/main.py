import os
import csv

# import csv data from Resources file
pybankCSV = os.path.join("Resources", "budget_data.csv")

# create empty lists
changeList = [] # create a list to store differences between each month
monthCount = 0 # month counter
total = 0
sumOfChanges = 0

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
        changeList.append(changeRevenue)
        previousRevenue = currentRevenue

    # slice the first element of the average revenue list because we do not cannot assume we start from 0 prior to the first date
    changeList = changeList[1:]

    # calculate sum
    for rev in changeList:
        sumOfChanges += rev

    # calculate average
    averageChange = sumOfChanges/len(changeList)

print(total)
print(averageChange)
print(len(changeList))






