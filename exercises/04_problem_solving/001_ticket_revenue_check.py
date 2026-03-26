ticket_sales = {
    "vip": {"tickets_sold": 650, "price": 250},
    "individual": {"tickets_sold": 18500, "price": 120},
    "subscriber": {"tickets_sold": 7200, "price": 90},
    "partner": {"tickets_sold": 1800, "price": 60}
}

revenue_target = 3000000
total_revenue = 0

for segment, data in ticket_sales.items():
    segment_revenue = data["tickets_sold"] * data["price"]
    total_revenue += segment_revenue

print("TICKET REVENUE CHECK")
print("--------------------")
print(f"Revenue target: {revenue_target} MAD")
print(f"Total revenue: {total_revenue} MAD")
print()

if total_revenue >= revenue_target:
    print("Revenue target reached.")
else:
    print("Revenue target not reached.")