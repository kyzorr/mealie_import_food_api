import requests
import json

# Konfiguration
MEALIE_URL = "<your_URL>"  # Passe ggf. die URL an
API_KEY = "<your_API_KEY>"              # Trage hier deinen API-Key ein
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

