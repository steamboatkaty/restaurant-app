from api import fetch_restaurants
from parser import format_restaurant

def main():
    restaurants = fetch_restaurants()
    top_10 = restaurants[:10]

    for restaurant in top_10:
        formatted = format_restaurant(restaurant)

        print(f"\n{formatted['name']}")
        print(f"Cuisines: {formatted['cuisines']}")
        print(f"Rating: {formatted['rating']}")
        print(f"Address: {formatted['address']}")

if __name__ == "__main__":
    main()