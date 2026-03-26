def validate_ticket_record(record):
    customer_name = record["customer_name"]
    tickets_sold = record["tickets_sold"]
    price = record["price"]

    if customer_name == "":
        return f"Invalid record: missing customer name -> {record}"
    if tickets_sold <= 0:
        return f"Invalid record: tickets sold must be greater than 0 -> {record}"
    if price <= 0:
        return f"Invalid record: price must be greater than 0 -> {record}"

    return f"Valid record -> {record}"


def print_validation_results(ticket_records):
    print("VALIDATE TICKET RECORDS")
    print("-----------------------")

    for record in ticket_records:
        validation_message = validate_ticket_record(record)
        print(validation_message)


def main():
    ticket_records = [
        {"customer_name": "Noureddine Serhir", "segment": "vip", "tickets_sold": 2, "price": 250},
        {"customer_name": "Nacer Laraki", "segment": "individual", "tickets_sold": 4, "price": 120},
        {"customer_name": "", "segment": "subscriber", "tickets_sold": 1, "price": 90},
        {"customer_name": "Reda Serhir", "segment": "partner", "tickets_sold": 0, "price": 60}
    ]

    print_validation_results(ticket_records)


if __name__ == "__main__":
    main()