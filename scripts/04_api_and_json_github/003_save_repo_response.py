import json
import requests


def fetch_public_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, timeout=10)

    return response.json()


def save_json_response(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def main():
    username = "redserlabs"
    file_name = "data/raw/api/github/repo_response.json"

    repositories = fetch_public_repositories(username)
    save_json_response(file_name, repositories)

    print("SAVE REPOSITORY RESPONSE")
    print("------------------------")
    print(f"GitHub username: {username}")
    print(f"JSON file created: {file_name}")
    print(f"Repositories saved: {len(repositories)}")


if __name__ == "__main__":
    main()