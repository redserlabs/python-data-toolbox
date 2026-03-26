import csv


def clean_ticket_row(row):
    return {
        "customer_name": row["customer_name"].strip().title(),
        "segment": row["segment"].strip().lower(),
        "tickets_sold": int(row["tickets_sold"]),
        "price": int(row["price"])
    }


def read_and_clean_ticket_sales(input_file):
    clean_ticket_sales = []

    with open(input_file, "r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            clean_row = clean_ticket_row(row)
            clean_ticket_sales.append(clean_row)

    return clean_ticket_sales


def export_clean_ticket_sales(output_file, clean_ticket_sales):
    with open(output_file, "w", newline="") as file:
        fieldnames = ["customer_name", "segment", "tickets_sold", "price"]
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

        csv_writer.writeheader()

        for row in clean_ticket_sales:
            csv_writer.writerow(row)


def main():
    input_file = "data/raw/ticket_sales.csv"
    output_file = "data/cleaned/clean_ticket_sales.csv"

    clean_ticket_sales = read_and_clean_ticket_sales(input_file)
    export_clean_ticket_sales(output_file, clean_ticket_sales)

    print("EXPORT CLEAN TICKET SALES CSV")
    print("-----------------------------")
    print(f"Clean file created: {output_file}")


if __name__ == "__main__":
    main()