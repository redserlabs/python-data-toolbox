import requests


def fetch_public_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, timeout=10)

    return response


def print_response_summary(username, response):
    print("FETCH PUBLIC REPOSITORIES")
    print("-------------------------")
    print(f"GitHub username: {username}")
    print(f"Status code: {response.status_code}")

    if response.status_code == 200:
        repositories = response.json()
        print(f"Repositories fetched: {len(repositories)}")
    else:
        print("Request failed.")


def main():
    username = "redserlabs"
    response = fetch_public_repositories(username)
    print_response_summary(username, response)


if __name__ == "__main__":
    main()