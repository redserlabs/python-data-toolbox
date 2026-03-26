def calculate_sales_summary(transformed_ticket_sales):
    total_tickets = 0
    total_revenue = 0

    for record in transformed_ticket_sales:
        total_tickets += record["tickets_sold"]
        total_revenue += record["total_amount"]

    return total_tickets, total_revenue


def build_summary_lines(transformed_ticket_sales, total_tickets, total_revenue):
    return [
        "SALES SUMMARY",
        "-------------",
        f"Total customers: {len(transformed_ticket_sales)}",
        f"Total tickets sold: {total_tickets}",
        f"Total revenue: {total_revenue} MAD"
    ]


def export_summary(file_name, summary_lines):
    with open(file_name, "w") as file:
        for line in summary_lines:
            file.write(line + "\n")


def read_summary(file_name):
    with open(file_name, "r") as file:
        return file.read()


def main():
    transformed_ticket_sales = [
        {"customer_name": "Noureddine Serhir", "segment": "vip", "tickets_sold": 2, "price": 250, "total_amount": 500},
        {"customer_name": "Nacer Laraki", "segment": "individual", "tickets_sold": 4, "price": 120, "total_amount": 480},
        {"customer_name": "Youssef Brahmi", "segment": "subscriber", "tickets_sold": 1, "price": 90, "total_amount": 90},
        {"customer_name": "Reda Serhir", "segment": "partner", "tickets_sold": 3, "price": 60, "total_amount": 180}
    ]

    file_name = "data/exports/sales_summary.txt"

    total_tickets, total_revenue = calculate_sales_summary(transformed_ticket_sales)
    summary_lines = build_summary_lines(transformed_ticket_sales, total_tickets, total_revenue)

    export_summary(file_name, summary_lines)
    summary_content = read_summary(file_name)

    print("EXPORT SALES SUMMARY")
    print("--------------------")
    print(summary_content)


if __name__ == "__main__":
    main()