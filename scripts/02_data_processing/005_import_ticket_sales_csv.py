import csv

file_name = "data/raw/ticket_sales.csv"

print("IMPORT TICKET SALES CSV")
print("-----------------------")

with open(file_name, "r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(row)