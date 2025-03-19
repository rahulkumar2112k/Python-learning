import requests
import random

def fetch_random_joke():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page=1"
    response = requests.get(url)
    data = response.json()

    if data.get("success") and "data" in data and "data" in data["data"]:
        jokes = data["data"]["data"]  # List of jokes
        if jokes:
            random_joke = random.choice(jokes)  # Select a random joke
            content = random_joke.get("content", "No joke content found.")
            return content
        else:
            raise Exception("No jokes found in the response.")
    else:
        raise Exception("Failed to fetch joke data")

def main():
    try:
        joke = fetch_random_joke()
        print(f"Here's a joke for you:\n{joke}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
