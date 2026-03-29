from api import fetch_restaurants
from parser import format_restaurant

def main():
    postcode = input("Enter a UK postcode: ")

    try:
        restaurants = fetch_restaurants(postcode)
       
        if not restaurants:
            print("No restaurants found for this postcode.")
            return

        top_10 = restaurants[:10]

        for restaurant in top_10:
            formatted = format_restaurant(restaurant)

            print(f"\n{formatted['name']}")
            print(f"Cuisines: {formatted['cuisines']}")
            print(f"Rating: {formatted['rating']}")
            print(f"Address: {formatted['address']}")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()