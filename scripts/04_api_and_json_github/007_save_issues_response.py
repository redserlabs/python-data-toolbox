import json
import requests


def fetch_repository_issues(owner, repo_name):
    url = f"https://api.github.com/repos/{owner}/{repo_name}/issues"
    response = requests.get(url, timeout=10)

    return response.json()


def save_json_response(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def main():
    owner = "microsoft"
    repo_name = "vscode"
    file_name = "data/raw/api/github/issues_response.json"

    issues = fetch_repository_issues(owner, repo_name)
    save_json_response(file_name, issues)

    print("SAVE ISSUES RESPONSE")
    print("--------------------")
    print(f"Repository: {owner}/{repo_name}")
    print(f"JSON file created: {file_name}")
    print(f"Issues saved: {len(issues)}")


if __name__ == "__main__":
    main()