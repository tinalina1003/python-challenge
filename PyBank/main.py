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

    sum = 0

    for i in range(len(valueList) - 1):
        difference = valueList[i + 1] - valueList[i]
        sum += difference

    return(sum/(len(valueList) - 1))


# extract data from csv file
with open(pybankCSV) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Skips the header (there is a header in this case)
    csv_header = next(csvreader)

    count = 0

    for row in csvreader:
        
        date.append(row[0])
        amount.append(int(row[1]))

        # this counts the total amount of dates
        count += 1


print(count)
print(change(amount))





