ticket_records = [
    {"customer_name": "Noureddine Serhir", "segment": "vip", "tickets_sold": 2, "price": 250},
    {"customer_name": "Nacer Laraki", "segment": "individual", "tickets_sold": 4, "price": 120},
    {"customer_name": "", "segment": "subscriber", "tickets_sold": 1, "price": 90},
    {"customer_name": "Reda Serhir", "segment": "partner", "tickets_sold": 0, "price": 60}
]

print("VALIDATE TICKET RECORDS")
print("-----------------------")

for record in ticket_records:
    customer_name = record["customer_name"]
    tickets_sold = record["tickets_sold"]
    price = record["price"]

    if customer_name == "":
        print(f"Invalid record: missing customer name -> {record}")
    elif tickets_sold <= 0:
        print(f"Invalid record: tickets sold must be greater than 0 -> {record}")
    elif price <= 0:
        print(f"Invalid record: price must be greater than 0 -> {record}")
    else:
        print(f"Valid record -> {record}")