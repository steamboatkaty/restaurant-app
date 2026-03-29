import requests

URL = "https://uk.api.just-eat.io/discovery/uk/restaurants/enriched/bypostcode/SE83NB"

def fetch_restaurants():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(URL, headers=headers)

    if response.status_code != 200:
        raise Exception("API request failed")

    data = response.json()
    return data["restaurants"]