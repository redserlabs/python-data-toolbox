import requests
from datetime import datetime


def fetch_repository_issues(owner, repo_name):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/issues"
    response = requests.get(url, timeout=10)

    return response.json()


def parse_github_datetime(date_string):
    return datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%SZ")


def filter_issues_by_date(issues, cutoff_date):
    filtered_issues = []

    for issue in issues:
        issue_created_at = parse_github_datetime(issue["created_at"])

        if issue_created_at >= cutoff_date:
            filtered_issues.append(issue)

    return filtered_issues


def print_issue_summary(filtered_issues):
    print("FILTER ISSUES BY DATE")
    print("---------------------")

    for issue in filtered_issues:
        issue_title = issue["title"]
        issue_created_at = issue["created_at"]

        print(f"Title: {issue_title}")
        print(f"Created at: {issue_created_at}")
        print()


def main():
    owner = "microsoft"
    repo_name = "vscode"
    cutoff_date = datetime(2025, 1, 1)

    issues = fetch_repository_issues(owner, repo_name)
    filtered_issues = filter_issues_by_date(issues, cutoff_date)

    print_issue_summary(filtered_issues)


if __name__ == "__main__":
    main()
