import requests


def get_user(username):
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return None


def display_user(data):
    print("\n" + "=" * 40)
    print(f"Name: {data['name']}")
    print(f"Location: {data['location']}")
    print(f"Followers: {data['followers']}")
    print(f"Following: {data['following']}")
    print(f"Public repos: {data['public_repos']}")
    print("=" * 40)


def main():
    username = input("GitHub username: ")

    data = get_user(username)

    if data:
        display_user(data)
    else:
        print("User not found.")


if __name__ == "__main__":
    main()