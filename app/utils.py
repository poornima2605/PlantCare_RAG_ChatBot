import requests
from typing import Optional

UNSPLASH_ACCESS_KEY = "wNCAXY59LZ2XduALKl23T6iocL5-dF4aQ4lLSiPWFs0"

def search_image(query: str) -> Optional[str]:
    url = "https://api.unsplash.com/search/photos"
    params = {
        "query": query,
        "client_id": UNSPLASH_ACCESS_KEY,
        "per_page": 1
    }
    response = requests.get(url, params=params)
    data = response.json()
    
    if data.get("results"):
        return data["results"][0]["urls"]["small"]
    return None

plant_keywords = ["rose", "tulip", "sunflower", "orchid", "fern", "basil", "cactus", "aloe"]

def extract_plant_name(text: str) -> Optional[str]:
    text = text.lower()
    for plant in plant_keywords:
        if plant in text:
            return plant
    return None
