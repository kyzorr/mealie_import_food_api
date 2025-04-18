import json
import requests

MEALIE_URL = "<YOUR_MEALIE_URL>"
API_KEY = "<YOUR_API_KEY>"
JSON_URL = "https://raw.githubusercontent.com/mealie-recipes/mealie/refs/heads/mealie-next/mealie/repos/seed/resources/foods/locales/de-DE.json" #original language json -> https://github.com/mealie-recipes/mealie/tree/mealie-next/mealie/repos/seed/resources/foods/locales

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.get(JSON_URL)
response.raise_for_status()
food_dict = response.json()

for key, value in food_dict.items():
    if isinstance(value, dict) and "name" in value:
        name = value["name"]
    elif isinstance(value, str):
        name = value
    else:
        continue

    food_obj = {
        "name": name,
        "pluralName": "",
        "description": "",
        "extras": {},
        "aliases": [],
        "householdsWithIngredientFood": []
    }

    api_response = requests.post(
        f"{MEALIE_URL}/api/foods",
        headers=headers,
        json=food_obj
    )
    if api_response.status_code == 201:
        print(f"Imported: {name}")
    else:
        print(f"Error by {name}: {api_response.status_code} {api_response.text}")
