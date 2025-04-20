import requests
import json
import os
from dotnev import load_dotenv

load_dotenv()

# Konfiguration
MEALIE_URL = os.getenv("MEALIE_URL") 
API_KEY = os.getenv("API_KEY") 
EXPORT_FILE = "mealie_foods_export_de_DE.json"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "accept": "application/json"
}

all_foods = []
page = 1
per_page = 50  # oder mehr, je nach API-Limit

while True:
    params = {"page": page, "perPage": per_page}
    response = requests.get(f"{MEALIE_URL}/api/foods", headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    items = data.get("items") or data.get("data") or data  # je nach API-Version
    if not items:
        break
    all_foods.extend(items)
    if len(items) < per_page:
        break
    page += 1

with open(EXPORT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_foods, f, indent=2, ensure_ascii=False)

print(f"Erfolgreich exportiert: {len(all_foods)} Lebensmittel in {EXPORT_FILE}")

