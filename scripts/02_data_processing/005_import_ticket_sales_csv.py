import csv


def read_ticket_sales_csv(file_name):
    ticket_sales = []

    with open(file_name, "r") as file:
        csv_reader = csv.DictReader(file)

        for row in csv_reader:
            ticket_sales.append(row)

    return ticket_sales


def print_ticket_sales_rows(ticket_sales):
    print("IMPORT TICKET SALES CSV")
    print("-----------------------")

    for row in ticket_sales:
        print(row)


def main():
    file_name = "data/raw/ticket_sales.csv"
    ticket_sales = read_ticket_sales_csv(file_name)
    print_ticket_sales_rows(ticket_sales)


if __name__ == "__main__":
    main()