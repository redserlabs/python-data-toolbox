report_date = "2026-06-12"
match_name = "Morocco vs France"
stadium_name = "Stade Mohammed V"

ticket_sales = {
    "vip": {"tickets_sold": 650, "price": 250},
    "individual": {"tickets_sold": 18500, "price": 120},
    "subscriber": {"tickets_sold": 7200, "price": 90},
    "partner": {"tickets_sold": 1800, "price": 60}
}

output_file = "data/exports/daily_sales_report.txt"

total_tickets_sold = 0
total_revenue = 0

for segment, data in ticket_sales.items():
    total_tickets_sold += data["tickets_sold"]
    total_revenue += data["tickets_sold"] * data["price"]

report_lines = [
    "DAILY SALES REPORT",
    "------------------",
    f"Report date: {report_date}",
    f"Match: {match_name}",
    f"Stadium: {stadium_name}",
    f"Total tickets sold: {total_tickets_sold}",
    f"Total revenue: {total_revenue} MAD"
]

with open(output_file, "w") as file:
    for line in report_lines:
        file.write(line + "\n")

print("CREATE DAILY SALES REPORT")
print("-------------------------")
print(f"Report created: {output_file}")