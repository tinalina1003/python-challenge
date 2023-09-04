import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

num_rows = 0
total_rev = 0
change_from_previous = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header:  {csv_header}")
    previous_revenue = 0

    for row in csvreader:
        revenue = int(row[1])
        num_rows += 1
        total_rev += revenue
        change_from_previous.append([row[0], revenue - previous_revenue])
        previous_revenue = revenue

print("")
print("There are "+ str(num_rows) +" months of data!")
print("Total Revenue is "+str(total_rev)+" dollars!")
print(change_from_previous)