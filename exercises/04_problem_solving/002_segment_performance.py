ticket_sales = {
    "vip": {"tickets_sold": 650, "price": 250},
    "individual": {"tickets_sold": 18500, "price": 120},
    "subscriber": {"tickets_sold": 7200, "price": 90},
    "partner": {"tickets_sold": 1800, "price": 60}
}

best_segment = ""
best_revenue = 0

for segment, data in ticket_sales.items():
    revenue = data["tickets_sold"] * data["price"]

    if revenue > best_revenue:
        best_segment = segment
        best_revenue = revenue

print("SEGMENT PERFORMANCE")
print("-------------------")
print(f"Best segment: {best_segment}")
print(f"Best revenue: {best_revenue} MAD")