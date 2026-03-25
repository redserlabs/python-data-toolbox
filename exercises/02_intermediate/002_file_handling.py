file_name = "data/exports/match_ticket_report.txt"

match_name = "Morocco vs France"
stadium_name = "Stade Mohammed V"
total_tickets_sold = 28150
total_revenue = 3494500

report_lines = [
    "MATCH TICKET REPORT",
    "-------------------",
    f"Match: {match_name}",
    f"Stadium: {stadium_name}",
    f"Total tickets sold: {total_tickets_sold}",
    f"Total revenue: {total_revenue} MAD"
]

with open(file_name, "w") as file:
    for line in report_lines:
        file.write(line + "\n")

with open(file_name, "r") as file:
    report_content = file.read()

print("FILE HANDLING")
print("-------------")
print(report_content)