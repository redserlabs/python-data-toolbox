def calculate_vip_revenue(ticket_sales):
    vip_tickets_sold = ticket_sales["vip"]["tickets_sold"]
    vip_ticket_price = ticket_sales["vip"]["price"]
    vip_revenue = vip_tickets_sold * vip_ticket_price

    return vip_tickets_sold, vip_ticket_price, vip_revenue


def print_vip_summary(match_name, vip_tickets_sold, vip_ticket_price, vip_revenue, vip_target_tickets):
    print("VIP SALES CHECK")
    print("---------------")
    print(f"Match: {match_name}")
    print(f"VIP tickets sold: {vip_tickets_sold}")
    print(f"VIP ticket price: {vip_ticket_price} MAD")
    print(f"VIP revenue: {vip_revenue} MAD")
    print(f"VIP target tickets: {vip_target_tickets}")
    print()

    if vip_tickets_sold >= vip_target_tickets:
        print("VIP sales target reached.")
    else:
        print("VIP sales target not reached.")


def main():
    match_name = "Morocco vs France"

    ticket_sales = {
        "individual": {"tickets_sold": 18500, "price": 120},
        "subscriber": {"tickets_sold": 7200, "price": 90},
        "partner": {"tickets_sold": 1800, "price": 60},
        "vip": {"tickets_sold": 650, "price": 250}
    }

    vip_target_tickets = 600
    vip_tickets_sold, vip_ticket_price, vip_revenue = calculate_vip_revenue(ticket_sales)

    print_vip_summary(
        match_name,
        vip_tickets_sold,
        vip_ticket_price,
        vip_revenue,
        vip_target_tickets
    )


if __name__ == "__main__":
    main()