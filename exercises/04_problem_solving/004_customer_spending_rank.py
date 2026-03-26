customer_ticket_sales = [
    {"customer_name": "Noureddine Serhir", "tickets_sold": 2, "price": 250},
    {"customer_name": "Nacer Laraki", "tickets_sold": 4, "price": 120},
    {"customer_name": "Youssef Brahmi", "tickets_sold": 1, "price": 90},
    {"customer_name": "Reda Serhir", "tickets_sold": 3, "price": 60}
]

top_customer = ""
top_spending = 0

for record in customer_ticket_sales:
    customer_name = record["customer_name"]
    total_spending = record["tickets_sold"] * record["price"]

    if total_spending > top_spending:
        top_customer = customer_name
        top_spending = total_spending

print("CUSTOMER SPENDING RANK")
print("----------------------")
print(f"Top customer: {top_customer}")
print(f"Top spending: {top_spending} MAD")