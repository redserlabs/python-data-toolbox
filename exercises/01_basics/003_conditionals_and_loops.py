tickets_sold = 42000

if tickets_sold >= 50000:
    print("Strong ticket sales")
else:
    print("Sales below target")

daily_ticket_sales = [3200, 4100, 3800, 4600, 5200]

for sales in daily_ticket_sales:
    print(sales)

matches = ["Morocco vs France", "Morocco vs Spain", "France vs Spain", "Spain vs Brazil"]

for match in matches:
    print(match)

channel_revenue = [120000, 85000, 210000, 95000]

for revenue in channel_revenue:
    if revenue >= 100000:
        print("High-performing sales channel")
    else:
        print("Standard-performing sales channel")