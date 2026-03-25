import random

home_team = "Morocco"
away_team = "France"
match_date = "2026-06-12"

home_code = home_team[:3].upper()
away_code = away_team[:3].upper()
date_code = match_date.replace("-", "")
random_code = random.randint(1000, 9999)

match_reference = f"{home_code}-{away_code}-{date_code}-{random_code}"

print("GENERATE MATCH REFERENCE")
print("------------------------")
print(f"Home team: {home_team}")
print(f"Away team: {away_team}")
print(f"Match date: {match_date}")
print(f"Match reference: {match_reference}")