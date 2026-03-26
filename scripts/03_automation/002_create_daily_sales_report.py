def calculate_daily_totals(ticket_sales):
    total_tickets_sold = 0
    total_revenue = 0

    for data in ticket_sales.values():
        total_tickets_sold += data["tickets_sold"]
        total_revenue += data["tickets_sold"] * data["price"]

    return total_tickets_sold, total_revenue


def build_daily_report_lines(report_date, match_name, stadium_name, total_tickets_sold, total_revenue):
    return [
        "DAILY SALES REPORT",
        "------------------",
        f"Report date: {report_date}",
        f"Match: {match_name}",
        f"Stadium: {stadium_name}",
        f"Total tickets sold: {total_tickets_sold}",
        f"Total revenue: {total_revenue} MAD"
    ]


def export_daily_report(output_file, report_lines):
    with open(output_file, "w") as file:
        for line in report_lines:
            file.write(line + "\n")


def main():
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

    total_tickets_sold, total_revenue = calculate_daily_totals(ticket_sales)
    report_lines = build_daily_report_lines(
        report_date,
        match_name,
        stadium_name,
        total_tickets_sold,
        total_revenue
    )

    export_daily_report(output_file, report_lines)

    print("CREATE DAILY SALES REPORT")
    print("-------------------------")
    print(f"Report created: {output_file}")


if __name__ == "__main__":
    main()