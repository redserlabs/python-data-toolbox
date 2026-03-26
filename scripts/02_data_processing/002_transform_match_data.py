def add_total_amount(record):
    total_amount = record["tickets_sold"] * record["price"]

    return {
        "customer_name": record["customer_name"],
        "segment": record["segment"],
        "tickets_sold": record["tickets_sold"],
        "price": record["price"],
        "total_amount": total_amount
    }


def transform_ticket_sales(clean_ticket_sales):
    transformed_ticket_sales = []

    for record in clean_ticket_sales:
        transformed_record = add_total_amount(record)
        transformed_ticket_sales.append(transformed_record)

    return transformed_ticket_sales


def print_transformed_ticket_sales(transformed_ticket_sales):
    print("TRANSFORM MATCH DATA")
    print("--------------------")

    for record in transformed_ticket_sales:
        print(record)


def main():
    clean_ticket_sales = [
        {"customer_name": "Noureddine Serhir", "segment": "vip", "tickets_sold": 2, "price": 250},
        {"customer_name": "Nacer Laraki", "segment": "individual", "tickets_sold": 4, "price": 120},
        {"customer_name": "Youssef Brahmi", "segment": "subscriber", "tickets_sold": 1, "price": 90},
        {"customer_name": "Reda Serhir", "segment": "partner", "tickets_sold": 3, "price": 60}
    ]

    transformed_ticket_sales = transform_ticket_sales(clean_ticket_sales)
    print_transformed_ticket_sales(transformed_ticket_sales)


if __name__ == "__main__":
    main()