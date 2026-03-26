def extract_vip_customers(ticket_sales):
    vip_customers = []

    for record in ticket_sales:
        if record["segment"] == "vip":
            vip_customers.append(record["customer_name"])

    return vip_customers


def export_vip_customer_list(output_file, vip_customers):
    with open(output_file, "w") as file:
        file.write("VIP CUSTOMER LIST\n")
        file.write("-----------------\n")

        for customer_name in vip_customers:
            file.write(customer_name + "\n")


def main():
    ticket_sales = [
        {"customer_name": "Noureddine Serhir", "segment": "vip"},
        {"customer_name": "Nacer Laraki", "segment": "individual"},
        {"customer_name": "Youssef Brahmi", "segment": "subscriber"},
        {"customer_name": "Reda Serhir", "segment": "partner"},
        {"customer_name": "Salma Bennani", "segment": "vip"}
    ]

    output_file = "data/exports/vip_customer_list.txt"

    vip_customers = extract_vip_customers(ticket_sales)
    export_vip_customer_list(output_file, vip_customers)

    print("SAVE VIP CUSTOMER LIST")
    print("----------------------")
    print(f"VIP customer file created: {output_file}")


if __name__ == "__main__":
    main()