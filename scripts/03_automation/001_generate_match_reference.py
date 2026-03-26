import random


def generate_team_code(team_name):
    return team_name[:3].upper()


def generate_date_code(match_date):
    return match_date.replace("-", "")


def generate_match_reference(home_team, away_team, match_date):
    home_code = generate_team_code(home_team)
    away_code = generate_team_code(away_team)
    date_code = generate_date_code(match_date)
    random_code = random.randint(1000, 9999)

    return f"{home_code}-{away_code}-{date_code}-{random_code}"


def print_match_reference_summary(home_team, away_team, match_date, match_reference):
    print("GENERATE MATCH REFERENCE")
    print("------------------------")
    print(f"Home team: {home_team}")
    print(f"Away team: {away_team}")
    print(f"Match date: {match_date}")
    print(f"Match reference: {match_reference}")


def main():
    home_team = "Morocco"
    away_team = "France"
    match_date = "2026-06-12"

    match_reference = generate_match_reference(home_team, away_team, match_date)
    print_match_reference_summary(home_team, away_team, match_date, match_reference)


if __name__ == "__main__":
    main()