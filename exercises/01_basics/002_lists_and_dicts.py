upcoming_matches = ["Morocco vs France", "Morocco vs Spain", "France vs Spain", "Spain vs Brazil"]
customer_segments = ["individual", "partner", "subscriber"]
sales_channels = ["website", "mobile_app", "box_office"]

print(upcoming_matches)
print(customer_segments)
print(sales_channels)

print(upcoming_matches[0])
print(customer_segments[-1])

ticketing_summary = {
    "match_name": "Morocco vs France",
    "stadium": "National Stadium",
    "tickets_sold": 42000,
    "average_ticket_price": 65.50
}

customer_profile = {
    "customer_id": 1001,
    "segment": "subscriber",
    "country": "Morocco"
}

sales_report = {
    "channel": "website",
    "orders": 18500,
    "revenue": 1215000
}

print(ticketing_summary)
print(ticketing_summary["match_name"])
print(ticketing_summary["tickets_sold"])

print(customer_profile["segment"])
print(sales_report["revenue"])