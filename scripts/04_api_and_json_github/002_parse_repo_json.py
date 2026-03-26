import requests


def fetch_public_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, timeout=10)

    return response.json()


def print_repository_details(repositories):
    print("PARSE REPOSITORY JSON")
    print("---------------------")

    for repo in repositories:
        repo_name = repo["name"]
        repo_language = repo["language"]
        repo_visibility = repo["visibility"]
        repo_created_at = repo["created_at"]

        print(f"Repository name: {repo_name}")
        print(f"Language: {repo_language}")
        print(f"Visibility: {repo_visibility}")
        print(f"Created at: {repo_created_at}")
        print()


def main():
    username = "redserlabs"
    repositories = fetch_public_repositories(username)
    print_repository_details(repositories)


if __name__ == "__main__":
    main()