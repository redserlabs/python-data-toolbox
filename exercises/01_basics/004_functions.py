def match_summary(match_name, tickets_sold, revenue):
    print(f"{match_name} sold {tickets_sold} tickets and generated {revenue} in revenue.")


def customer_summary(customer_id, segment):
    print(f"Customer {customer_id} belongs to the {segment} segment.")


def total_revenue(revenue_list):
    total = 0
    for revenue in revenue_list:
        total = total + revenue
    return total


match_summary("Morocco vs France", 42000, 2751000)
customer_summary(1001, "subscriber")

match_revenues = [120000, 85000, 210000, 95000]
print(total_revenue(match_revenues))