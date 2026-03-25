import csv

file_name = "data/raw/ticket_sales.csv"

clean_ticket_sales = []

print("CLEAN TICKET SALES CSV")
print("----------------------")

with open(file_name, "r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        clean_row = {
            "customer_name": row["customer_name"].strip().title(),
            "segment": row["segment"].strip().lower(),
            "tickets_sold": int(row["tickets_sold"]),
            "price": int(row["price"])
        }
        clean_ticket_sales.append(clean_row)

for row in clean_ticket_sales:
    print(row)