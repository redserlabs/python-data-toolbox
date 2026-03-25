match_name = "Morocco vs France"

ticket_sales = {
    "individual": {"tickets_sold": 18500, "price": 120},
    "subscriber": {"tickets_sold": 7200, "price": 90},
    "partner": {"tickets_sold": 1800, "price": 60},
    "vip": {"tickets_sold": 650, "price": 250}
}

segment_revenues = {}

for segment, data in ticket_sales.items():
    tickets_sold = data["tickets_sold"]
    price = data["price"]
    revenue = tickets_sold * price
    segment_revenues[segment] = revenue

top_segment = ""
top_revenue = 0

for segment, revenue in segment_revenues.items():
    if revenue > top_revenue:
        top_segment = segment
        top_revenue = revenue

print("SEGMENT REVENUE REPORT")
print("----------------------")
print(f"Match: {match_name}")
print()

for segment, revenue in segment_revenues.items():
    print(f"{segment}: {revenue} MAD")

print()
print(f"Top revenue segment: {top_segment}")
print(f"Top revenue amount: {top_revenue} MAD")