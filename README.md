# Mealie Food Import/Export Tools

## Inhaltsverzeichnis

- [Deutsch](#deutsch)
  - [Funktionen](#funktionen)
  - [Download & Installation](#download--installation)
  - [Anwendung](#anwendung)
  - [Beispiel-Export](#beispiel-export)
  - [Credits](#credits)
- [English](#english)
  - [Features](#features)
  - [Download & Setup](#download--setup)
  - [Usage](#usage)
  - [Example Export](#example-export)
  - [Credits](#credits-1)

---

## Deutsch

Dieses Projekt stellt Tools zum **Importieren und Exportieren von Lebensmitteln** aus einer [Mealie](https://mealie.io/) Instanz bereit.  
Mit jedem Release werden ausführbare Windows-Dateien (`.exe`) für Import und Export sowie eine Beispiel-Konfigurationsdatei bereitgestellt.

### Funktionen

- **Export:** Exportiere alle Lebensmittel deiner Mealie-Instanz als JSON-Datei.
- **Import:** Importiere Lebensmittel aus einer JSON-Datei in deine Mealie-Instanz.

### Download & Installation

1. **Gehe zum [Releases-Bereich](https://github.com/kyzorr/mealie_import_food_api/releases) dieses Repositories.**
2. **Lade die gewünschte ZIP-Datei herunter:**
   - `Food_export_package.zip` für den Export
   - `Food_import_package.zip` für den Import
3. **Entpacke die ZIP-Datei** in einen beliebigen Ordner.
4. **Benenne die Datei `.env.example` in `.env` um.**
5. **Öffne die `.env`-Datei** und trage deine Mealie-URL sowie deinen API-Key ein:
```

MEALIE_URL=https://deine-mealie-url.de
MEALIE_API_KEY=dein_api_key

```

### Anwendung

- **Export:**  
Starte `Food_export.exe` per Doppelklick oder über die Kommandozeile.  
Beispiel (Kommandozeile):
```

Food_export.exe --export mealie-export.json

```

- **Import:**  
Starte `Food_import.exe` per Doppelklick oder über die Kommandozeile.  
Beispiel (Kommandozeile):
```

Food_import.exe --import de_DE.json

```

### Beispiel-Export

Eine Beispiel-JSON mit deutschen Lebensmitteln (`de_DE.json`) ist im Repository enthalten und kann als Vorlage für den Import verwendet werden.

### Credits

- Dieses Projekt basiert auf der [Mealie](https://mealie.io/) API.
- Besonderer Dank an den Mealie-Projektersteller!
- Die originalen Lebensmittel-JSON-Dateien für verschiedene Sprachen gibt es in dem offiziellen Mealie Repository:  
[Mealie Food Localizations](https://github.com/mealie-recipes/mealie/tree/mealie-next/mealie/repos/seed/resources/foods/locales).

---

## English

This project provides tools to **import and export foods** from a [Mealie](https://mealie.io/) instance.  
Each release includes ready-to-use Windows executables (`.exe`) for import and export, plus an example configuration file.

### Features

- **Export:** Export all foods from your Mealie instance as a JSON file.
- **Import:** Import foods from a JSON file into your Mealie instance.

### Download & Setup

1. **Go to the [Releases section](https://github.com/kyzorr/mealie_import_food_api/releases) of this repository.**
2. **Download the desired ZIP file:**
 - `Food_export_package.zip` for export
 - `Food_import_package.zip` for import
3. **Extract the ZIP file** to any folder.
4. **Rename the `.env.example` file to `.env`.**
5. **Open the `.env` file** and enter your Mealie URL and API key:
```

MEALIE_URL=https://your-mealie-url.com
MEALIE_API_KEY=your_api_key

```

### Usage

- **Export:**  
Start `Food_export.exe` by double-clicking or from the command line.  
Example (command line):
```

Food_export.exe --export mealie-export.json

```

- **Import:**  
Start `Food_import.exe` by double-clicking or from the command line.  
Example (command line):
```

Food_import.exe --import de_DE.json

```

### Example Export

A sample JSON file with German foods (`de_DE.json`) is included in the repository and can be used as a template for importing.

### Credits

- This project is based on the [Mealie](https://mealie.io/) API.
- Special thanks to the creator of Mealie!
- The original food JSON files for various languages can you find in the official Mealie repository:  
[Mealie Food Localizations](https://github.com/mealie-recipes/mealie/tree/mealie-next/mealie/repos/seed/resources/foods/locales).

---
