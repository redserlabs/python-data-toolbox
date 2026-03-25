ticket_price = "120"
tickets_requested = "three"

print("ERROR HANDLING")
print("--------------")

try:
    total_price = int(ticket_price) * int(tickets_requested)
    print(f"Total price: {total_price} MAD")
except ValueError:
    print("Invalid input: ticket price and tickets requested must be numbers.")