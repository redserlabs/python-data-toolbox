customer_full_name = "   reda serhir   "
customer_email = "REDA.SERHIR@GMAIL.COM "
ticket_category = " vip "
match_city = "casablanca"

clean_full_name = customer_full_name.strip().title()
clean_email = customer_email.strip().lower()
clean_ticket_category = ticket_category.strip().upper()
clean_match_city = match_city.strip().title()

email_domain = clean_email.split("@")[1]
customer_first_name = clean_full_name.split()[0]

print("STRING PROCESSING")
print("-----------------")
print(f"Raw full name: '{customer_full_name}'")
print(f"Clean full name: {clean_full_name}")
print()
print(f"Raw email: '{customer_email}'")
print(f"Clean email: {clean_email}")
print(f"Email domain: {email_domain}")
print()
print(f"Raw ticket category: '{ticket_category}'")
print(f"Clean ticket category: {clean_ticket_category}")
print()
print(f"Raw match city: '{match_city}'")
print(f"Clean match city: {clean_match_city}")
print()
print(f"Customer first name: {customer_first_name}")
print(f"Name length: {len(clean_full_name)} characters")