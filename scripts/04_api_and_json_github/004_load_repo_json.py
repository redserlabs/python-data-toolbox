import json


def load_json_file(file_name):
    with open(file_name, "r") as file:
        return json.load(file)


def print_repository_details(repositories):
    print("LOAD REPOSITORY JSON FILE")
    print("-------------------------")

    for repo in repositories:
        repo_name = repo["name"]
        repo_visibility = repo["visibility"]
        repo_created_at = repo["created_at"]

        print(f"Repository name: {repo_name}")
        print(f"Visibility: {repo_visibility}")
        print(f"Created at: {repo_created_at}")
        print()


def main():
    file_name = "data/raw/api/github/repo_response.json"
    repositories = load_json_file(file_name)
    print_repository_details(repositories)


if __name__ == "__main__":
    main()