ticket_sales = {
    "vip": {"tickets_sold": 650, "price": 250},
    "individual": {"tickets_sold": 18500, "price": 120},
    "subscriber": {"tickets_sold": 7200, "price": 90},
    "partner": {"tickets_sold": 1800, "price": 60}
}

segment_summary = {}

for segment, data in ticket_sales.items():
    tickets_sold = data["tickets_sold"]
    price = data["price"]
    revenue = tickets_sold * price

    segment_summary[segment] = {
        "tickets_sold": tickets_sold,
        "price": price,
        "revenue": revenue
    }

print("SEGMENT SUMMARY DICTIONARY")
print("--------------------------")

for segment, summary in segment_summary.items():
    print(f"Segment: {segment}")
    print(f"Tickets sold: {summary['tickets_sold']}")
    print(f"Price: {summary['price']} MAD")
    print(f"Revenue: {summary['revenue']} MAD")
    print()