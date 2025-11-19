from functools import lru_cache

import requests


@lru_cache(maxsize=None)
def get_valid_cat_breeds():
    """Fetch valid cat breeds from TheCatAPI"""
    try:
        response = requests.get("https://api.thecatapi.com/v1/breeds", timeout=5)
        if response.status_code == 200:
            breeds = response.json()
            return {breed["name"].lower() for breed in breeds}
    except Exception as e:
        print(f"Error fetching cat breeds: {e}")
    return set()


def validate_cat_breed(breed):
    """Validate if the breed exists in TheCatAPI"""
    valid_breeds = get_valid_cat_breeds()
    if not valid_breeds:
        # If API fails, allow any breed
        return True
    return breed.lower() in valid_breeds
