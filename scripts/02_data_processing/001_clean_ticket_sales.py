def clean_ticket_record(record):
    return {
        "customer_name": record["customer_name"].strip().title(),
        "segment": record["segment"].strip().lower(),
        "tickets_sold": int(record["tickets_sold"]),
        "price": int(record["price"])
    }


def clean_ticket_sales_records(raw_ticket_sales):
    clean_ticket_sales = []

    for record in raw_ticket_sales:
        clean_record = clean_ticket_record(record)
        clean_ticket_sales.append(clean_record)

    return clean_ticket_sales


def print_clean_ticket_sales(clean_ticket_sales):
    print("CLEAN TICKET SALES")
    print("------------------")

    for record in clean_ticket_sales:
        print(record)


def main():
    raw_ticket_sales = [
        {"customer_name": " noureddine serhir ", "segment": " vip ", "tickets_sold": "2", "price": "250"},
        {"customer_name": " nacer laraki ", "segment": " individual ", "tickets_sold": "4", "price": "120"},
        {"customer_name": " youssef brahmi ", "segment": " subscriber ", "tickets_sold": "1", "price": "90"},
        {"customer_name": " reda serhir ", "segment": " partner ", "tickets_sold": "3", "price": "60"}
    ]

    clean_ticket_sales = clean_ticket_sales_records(raw_ticket_sales)
    print_clean_ticket_sales(clean_ticket_sales)


if __name__ == "__main__":
    main()