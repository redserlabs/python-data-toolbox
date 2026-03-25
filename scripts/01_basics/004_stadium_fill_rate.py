match_name = "Morocco vs France"
stadium_name = "Stade Mohammed V"
stadium_capacity = 45000

ticket_sales = {
    "individual": {"tickets_sold": 18500, "price": 120},
    "subscriber": {"tickets_sold": 7200, "price": 90},
    "partner": {"tickets_sold": 1800, "price": 60},
    "vip": {"tickets_sold": 650, "price": 250}
}

total_tickets_sold = 0

for segment, data in ticket_sales.items():
    total_tickets_sold += data["tickets_sold"]

fill_rate = (total_tickets_sold / stadium_capacity) * 100

print("STADIUM FILL RATE")
print("-----------------")
print(f"Match: {match_name}")
print(f"Stadium: {stadium_name}")
print(f"Capacity: {stadium_capacity}")
print(f"Total tickets sold: {total_tickets_sold}")
print(f"Fill rate: {fill_rate:.2f}%")

print()

if fill_rate >= 90:
    print("Excellent occupancy level.")
elif fill_rate >= 75:
    print("Strong occupancy level.")
else:
    print("Occupancy level can be improved.")