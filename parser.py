def format_restaurant(restaurant):
    name = restaurant["name"]

    cuisines_list = restaurant["cuisines"]
    cuisines = [cuisine["name"] for cuisine in cuisines_list]

    rating = restaurant["rating"].get("starRating", "N/A")

    address_data = restaurant["address"]
    address = f"{address_data['firstLine']}, {address_data['city']}, {address_data['postalCode']}"

    return {
        "name": name,
        "cuisines": ", ".join(cuisines),
        "rating": rating,
        "address": address
    }