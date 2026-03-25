match_data = {
    "match_name": "Morocco vs France",
    "stadium": {
        "name": "Stade Mohammed V",
        "city": "Casablanca",
        "capacity": 45000
    },
    "ticket_sales": {
        "vip": {"tickets_sold": 650, "price": 250},
        "individual": {"tickets_sold": 18500, "price": 120},
        "subscriber": {"tickets_sold": 7200, "price": 90},
        "partner": {"tickets_sold": 1800, "price": 60}
    }
}

stadium_name = match_data["stadium"]["name"]
stadium_city = match_data["stadium"]["city"]
vip_tickets = match_data["ticket_sales"]["vip"]["tickets_sold"]
vip_price = match_data["ticket_sales"]["vip"]["price"]

print("NESTED TICKET DATA")
print("------------------")
print(f"Match: {match_data['match_name']}")
print(f"Stadium: {stadium_name}")
print(f"City: {stadium_city}")
print(f"VIP tickets sold: {vip_tickets}")
print(f"VIP price: {vip_price} MAD")