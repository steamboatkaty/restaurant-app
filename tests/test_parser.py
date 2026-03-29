import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from parser import format_restaurant

def test_format_restaurant():
    sample_data = {
        "name": "Test Restaurant",
        "cuisines": [{"name": "Italian"}, {"name": "Pizza"}],
        "rating": {"starRating": 4.5},
        "address": {
            "firstLine": "123 Test Street",
            "city": "London",
            "postalCode": "SE1 1AA"
        }
    }

    result = format_restaurant(sample_data)

    assert result["name"] == "Test Restaurant"
    assert result["cuisines"] == "Italian, Pizza"
    assert result["rating"] == 4.5
    assert result["address"] == "123 Test Street, London, SE1 1AA"