match_name = "Morocco vs France"
stadium_name = "Stade Mohammed V"
match_date = "2026-06-12"

ticket_sales = {
    "individual": {"tickets_sold": 18500, "price": 120},
    "subscriber": {"tickets_sold": 7200, "price": 90},
    "partner": {"tickets_sold": 1800, "price": 60},
    "vip": {"tickets_sold": 650, "price": 250}
}

total_tickets_sold = 0
total_revenue = 0

for segment, data in ticket_sales.items():
    segment_tickets = data["tickets_sold"]
    segment_price = data["price"]
    segment_revenue = segment_tickets * segment_price

    total_tickets_sold += segment_tickets
    total_revenue += segment_revenue

print("MATCHDAY TICKET SUMMARY")
print("-----------------------")
print(f"Match: {match_name}")
print(f"Stadium: {stadium_name}")
print(f"Date: {match_date}")
print()

for segment, data in ticket_sales.items():
    segment_tickets = data["tickets_sold"]
    segment_price = data["price"]
    segment_revenue = segment_tickets * segment_price

    print(f"Segment: {segment}")
    print(f"Tickets sold: {segment_tickets}")
    print(f"Price per ticket: {segment_price} MAD")
    print(f"Revenue: {segment_revenue} MAD")
    print()

print("-----------------------")
print(f"Total tickets sold: {total_tickets_sold}")
print(f"Total revenue: {total_revenue} MAD")