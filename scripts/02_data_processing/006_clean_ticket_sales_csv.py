import csv


def clean_ticket_row(row):
    return {
        "customer_name": row["customer_name"].strip().title(),
        "segment": row["segment"].strip().lower(),
        "tickets_sold": int(row["tickets_sold"]),
        "price": int(row["price"])
    }


def read_and_clean_ticket_sales_csv(file_name):
    clean_ticket_sales = []

    with open(file_name, "r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            clean_row = clean_ticket_row(row)
            clean_ticket_sales.append(clean_row)

    return clean_ticket_sales


def print_clean_ticket_sales(clean_ticket_sales):
    print("CLEAN TICKET SALES CSV")
    print("----------------------")

    for row in clean_ticket_sales:
        print(row)


def main():
    file_name = "data/raw/ticket_sales.csv"
    clean_ticket_sales = read_and_clean_ticket_sales_csv(file_name)
    print_clean_ticket_sales(clean_ticket_sales)


if __name__ == "__main__":
    main()