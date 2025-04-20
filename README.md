# Mealie Lebensmittel Import/Export API

## Deutsch

Dieses Projekt bietet eine API zum Importieren und Exportieren von Lebensmitteln aus einer [Mealie](https://mealie.io/) Instanz. Es verwendet die Mealie API, um Lebensmitteldaten zu verwalten.

### Funktionen

-   **Import**: Importiere Lebensmittel aus einer JSON-Datei in deine Mealie Instanz.
-   **Export**: Exportiere alle Lebensmittel deiner Mealie Instanz als JSON-Datei.

### Voraussetzungen

-   Python 3.6 oder höher
-   Eine laufende Mealie Instanz
-   [requests](https://pypi.org/project/requests/) Python Bibliothek (Installation mit `pip install requests`)

### Konfiguration

Erstelle eine `.env`-Datei im Projektverzeichnis und trage folgende Variablen ein:

```

MEALIE_URL=https://deine-mealie-url.de
MEALIE_API_KEY=dein_api_key

```

### Verwendung

1.  Installiere die benötigten Python Pakete:

    ```
    pip install requests
    ```

2.  Konfiguriere die `.env`-Datei mit deiner Mealie URL und API Key.
3.  Führe das Skript `main.py` mit den entsprechenden Argumenten aus:

    -   Um Lebensmittel zu importieren:

        ```
        python main.py --import &lt;pfad_zur_json_datei&gt;
        ```

    -   Um Lebensmittel zu exportieren:

        ```
        python main.py --export &lt;pfad_zur_export_datei&gt;
        ```

### Beispiel-Export

Eine Beispiel-JSON mit deutschen Lebensmitteln (`mealie_foods_export_de_DE.json`) ist im Repository enthalten. Diese Datei kann als Vorlage für den Import verwendet werden.

### Credits

Dieses Projekt verwendet Daten und Konzepte aus dem [Mealie Projekt](https://mealie.io/). Ein besonderer Dank geht an den Ersteller von Mealie für die Bereitstellung dieser großartigen Rezeptverwaltungssoftware.

Die originalen Lebensmittel-JSON-Dateien für verschiedene Sprachen stammen aus dem offiziellen Mealie Repository: [Mealie Lebensmittel Lokalisierungen](https://github.com/mealie-recipes/mealie/tree/mealie-next/mealie/repos/seed/resources/foods/locales).

## English

This project provides an API to import and export foods from a [Mealie](https://mealie.io/) instance. It uses the Mealie API to manage food data.

### Features

-   **Import**: Import foods from a JSON file into your Mealie instance.
-   **Export**: Export all foods from your Mealie instance as a JSON file.

### Requirements

-   Python 3.6 or higher
-   A running Mealie instance
-   [requests](https://pypi.org/project/requests/) Python library (Install with `pip install requests`)

### Configuration

Create a `.env` file in the project directory and enter the following variables:

```

MEALIE_URL=https://your-mealie-url.com
MEALIE_API_KEY=your_api_key

```

### Usage

1.  Install the required Python packages:

    ```
    pip install requests
    ```

2.  Configure the `.env` file with your Mealie URL and API key.
3.  Run the `main.py` script with the appropriate arguments:

    -   To import foods:

        ```
        python main.py --import &lt;path_to_json_file&gt;
        ```

    -   To export foods:

        ```
        python main.py --export &lt;path_to_export_file&gt;
        ```

### Example Export

A sample JSON file with German foods (`mealie_foods_export_de_DE.json`) is included in the repository. This file can be used as a template for importing.

### Credits

This project uses data and concepts from the [Mealie Project](https://mealie.io/). Special thanks to the creator of Mealie for providing this great recipe management software.

The original food JSON files for various languages come from the official Mealie repository: [Mealie Food Localizations](https://github.com/mealie-recipes/mealie/tree/mealie-next/mealie/repos/seed/resources/foods/locales).