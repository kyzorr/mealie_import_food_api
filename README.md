# Mealie Food Import Script (German below)

This script imports foods into a Mealie instance using the Mealie API.

## Prerequisites

*   Python 3.6 or higher
*   The `requests` library (`pip install requests`)
*   A running Mealie instance
*   An API key for your Mealie instance

## Setup

1.  **Download the Script:** Save `mealie_import.py` to a directory of your choice.
2.  **Configuration:**
    *   Open `mealie_import.py` in a text editor.
    *   Replace `YOUR_MEALIE_URL` with your Mealie instance URL (e.g., `https://my-mealie-instance.com`).
    *   Replace `YOUR_API_KEY` with your personal Mealie API key.
3.  **JSON Source:**  
    The script downloads food data from:  
    `https://github.com/mealie-recipes/mealie/tree/mealie-next/mealie/repos/seed/resources/foods/locales`
    *   The file `de-DE.json` contains German food names. You can change the URL to use another language file.
4.  **API Endpoint:**  
    The script uses the `/api/foods` endpoint to import foods.

## Usage

1.  Open a terminal or command prompt.
2.  Navigate to the directory where you saved the script.
3.  Run the script with `python mealie_import.py`.
4.  The script will print the status of each import.

## Important Notes

*   **API Key:** Make sure your API key has permission to create foods in your Mealie instance.
*   **Data Structure:**  
    The script expects the JSON file to provide a list of food objects in the following format:

    ```
    {
      "name": "Food Name",
      "pluralName": "",
      "description": "",
      "extras": {},
      "aliases": [],
      "householdsWithIngredientFood": []
    }
    ```

    Adjust the script if your JSON source has a different structure.
*   **Error Handling:**  
    The script will print error messages if an import fails. Check the output to troubleshoot.
*   **Rate Limiting:**  
    Mealie may apply rate limits to API requests. If importing many foods, consider adding a short delay between requests (e.g., `time.sleep(0.1)`).

## Disclaimer

This script is provided as-is, without warranty. Use at your own risk.


---
---
---

# Mealie Lebensmittel-Importskript

Dieses Skript importiert Lebensmittel in eine Mealie-Instanz mithilfe der Mealie-API.

## Voraussetzungen

*   Python 3.6 oder höher
*   `requests` Bibliothek (installiere mit `pip install requests`)
*   Eine laufende Mealie-Instanz
*   API-Key für deine Mealie-Instanz

## Einrichtung

1.  **Skript herunterladen:** Lade das Skript `mealie_import.py` in ein Verzeichnis deiner Wahl herunter.
2.  **Konfiguration:**
    *   Öffne die Datei `mealie_import.py` in einem Texteditor.
    *   Ersetze `YOUR_MEALIE_URL` durch die URL deiner Mealie-Instanz (z.B. `https://meine-mealie-instanz.de`).
    *   Ersetze `YOUR_API_KEY` durch deinen persönlichen Mealie-API-Key.
3.  **JSON-Quelle:** Das Skript lädt die Lebensmitteldaten von:  
    `https://github.com/mealie-recipes/mealie/tree/mealie-next/mealie/repos/seed/resources/foods/locales`
    *   Die Datei `de-DE.json` enthält die deutschen Lebensmittelnamen. Du kannst die URL zu einer anderen Sprachdatei anpassen.
4.  **API-Endpoint:** Das Skript verwendet den Mealie-API-Endpoint `/api/foods` zum Importieren der Lebensmittel.

## Verwendung

1.  Öffne ein Terminal oder eine Kommandozeile.
2.  Navigiere in das Verzeichnis, in dem du das Skript gespeichert hast.
3.  Führe das Skript mit dem Befehl `python mealie_import.py` aus.
4.  Das Skript gibt den Status jedes Imports aus.

## Wichtige Hinweise

*   **API-Key:** Stelle sicher, dass dein API-Key die Berechtigung hat, Lebensmittel in deiner Mealie-Instanz anzulegen.
*   **Datenstruktur:** Das Skript geht davon aus, dass die JSON-Datei eine Liste von Lebensmittelobjekten im folgenden Format enthält:

    ```
    {
      "name": "Lebensmittelname",
      "pluralName": "",
      "description": "",
      "extras": {},
      "aliases": [],
      "householdsWithIngredientFood": []
    }
    ```

    Passe das Skript an, wenn deine JSON-Datei eine andere Struktur hat.
*   **Fehlerbehandlung:** Das Skript gibt Fehlermeldungen aus, wenn ein Import fehlschlägt. Überprüfe die Meldungen, um das Problem zu beheben.
*   **Ratenbegrenzung:** Mealie kann eine Ratenbegrenzung für API-Anfragen haben. Wenn du viele Lebensmittel importierst, kann es sinnvoll sein, eine kurze Pause zwischen den Anfragen einzubauen (z.B. mit `time.sleep(0.1)`).

## Disclaimer

Dieses Skript wird ohne Gewähr zur Verfügung gestellt. Die Verwendung erfolgt auf eigene Gefahr.
