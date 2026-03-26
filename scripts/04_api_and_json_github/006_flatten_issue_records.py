import requests


def fetch_repository_issues(owner, repo_name):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/issues"
    response = requests.get(url, timeout=10)

    return response.json()


def flatten_issue_records(issues):
    flattened_issues = []

    for issue in issues:
        issue_record = {
            "issue_id": issue["id"],
            "issue_number": issue["number"],
            "title": issue["title"],
            "state": issue["state"],
            "created_at": issue["created_at"],
            "user_login": issue["user"]["login"]
        }

        flattened_issues.append(issue_record)

    return flattened_issues


def print_flattened_issues(flattened_issues):
    print("FLATTEN ISSUE RECORDS")
    print("---------------------")

    for issue in flattened_issues:
        print(issue)


def main():
    owner = "microsoft"
    repo_name = "vscode"

    issues = fetch_repository_issues(owner, repo_name)
    flattened_issues = flatten_issue_records(issues)

    print_flattened_issues(flattened_issues)


if __name__ == "__main__":
    main()