stadium_name = "Stade Mohammed V"
stadium_capacity = 45000

ticket_sales = {
    "vip": {"tickets_sold": 650, "price": 250},
    "individual": {"tickets_sold": 18500, "price": 120},
    "subscriber": {"tickets_sold": 7200, "price": 90},
    "partner": {"tickets_sold": 1800, "price": 60}
}

total_tickets_sold = 0

for segment, data in ticket_sales.items():
    total_tickets_sold += data["tickets_sold"]

remaining_capacity = stadium_capacity - total_tickets_sold

print("MATCH CAPACITY ALERT")
print("--------------------")
print(f"Stadium: {stadium_name}")
print(f"Capacity: {stadium_capacity}")
print(f"Total tickets sold: {total_tickets_sold}")
print(f"Remaining capacity: {remaining_capacity}")
print()

if remaining_capacity <= 5000:
    print("Alert: stadium is close to full capacity.")
else:
    print("Capacity level is still under control.")