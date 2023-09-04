import os
import csv

# import csv data from Resources file
pybankCSV = os.path.join("Resources", "budget_data.csv")

# create empty lists
date = []
amount = []

# create a function that calculates total
def total(amountList):

    netTotal = 0

    for budget in amountList:
        netTotal += budget

    return netTotal

def change(valueList):

    for i in range(len(valueList)):
        for j in valueList:
            difference = valueList[j + 1] - valueList[j]
    
    print(difference)


# extract data from csv file
with open(pybankCSV) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Skips the header (there is a header in this case)
    csv_header = next(csvreader)

    count = 0

    for row in csvreader:

        date.append(row[0])
        amount.append(float(row[1]))

        # this counts the total amount of dates
        count += 1


print(count)
change(amount)




