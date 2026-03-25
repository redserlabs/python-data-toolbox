import csv

input_file = "data/raw/ticket_sales.csv"
output_file = "data/cleaned/clean_ticket_sales.csv"

clean_ticket_sales = []

with open(input_file, "r") as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        clean_row = {
            "customer_name": row["customer_name"].strip().title(),
            "segment": row["segment"].strip().lower(),
            "tickets_sold": int(row["tickets_sold"]),
            "price": int(row["price"])
        }
        clean_ticket_sales.append(clean_row)

with open(output_file, "w", newline="") as file:
    fieldnames = ["customer_name", "segment", "tickets_sold", "price"]
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()

    for row in clean_ticket_sales:
        csv_writer.writerow(row)

print("EXPORT CLEAN TICKET SALES CSV")
print("-----------------------------")
print(f"Clean file created: {output_file}")