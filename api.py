import requests

BASE_URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/"

def fetch_restaurants(postcode):
    url = BASE_URL + postcode.replace(" ", "")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("API request failed")

    data = response.json()
    return data["restaurants"]