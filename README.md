# Meteo Catalunya

Meteo Catalunya is a Django web application created as a CS50W Final Project.  
The goal of the project is to provide mountain and weather information for ski resorts and main summits in Catalunya, with an interactive map and weather data.

> **Project status:** Work in progress.  
> Some features are already implemented, while others are still being developed or improved.

---

## Overview

The application focuses on mountain weather in Catalunya, especially around the Pyrenees.  
At the moment, the project includes pages for:

- Ski resorts in Catalunya
- Main summits in Catalunya
- Interactive maps using Leaflet
- Resort and summit cards
- Weather information using the Open-Meteo API

The idea is to make it easy to check useful mountain information such as location, elevation, temperature, snowfall, and general conditions.

---

## Features implemented so far

### Ski Resorts page

The Ski Resorts page displays a list of ski resorts in Catalunya with an interactive map.

Current functionality includes:

- Resort cards displayed on the left and right sides of the map
- Leaflet map in the center of the page
- Markers for each ski resort
- Card and marker interaction:
  - Clicking a card moves the map to the resort
  - Clicking a marker highlights the corresponding card
- Responsive layout using Bootstrap
- Resort data stored in the database
- Weather information fetched from the Open-Meteo API

Example resorts included:

- La Molina
- Masella
- Baqueira Beret
- Boí Taüll
- Espot
- Port Ainé
- Vall de Núria
- Port del Comte
- Tavascán

---

### Main Summits page

The Main Summits page is being developed to show important mountain summits in Catalunya.

The objective is to provide information about the highest or most representative summits in different areas of the Catalan Pyrenees.

Current/planned information for each summit includes:

- Name
- Slug
- Top elevation
- Latitude
- Longitude
- Region or mountain area
- Short description
- Map marker

Example summits planned or added:

- Pica d'Estats
- Pic de Comaloforno
- Tuc de Molières
- Pic de Comalesbienes
- Pic de Peguera
- Puigpedrós
- Montardo
- Tuc de Cigalera
- La Tosa
- Pedraforca
- Tossa Plana de Lles
- Puig d'Alp
- Pic de Filià
- Monteixo
- Pics de Bassiero
- Mont-roig
- Pic de Certascan
- Pic de Ventolau
- Bastiments
- Montsent de Pallars

---

## Technologies used

This project uses:

- Python
- Django
- HTML
- CSS
- JavaScript
- Bootstrap
- Leaflet.js
- OpenStreetMap tiles
- Open-Meteo API
- SQLite

---

## Project structure

The main Django app is called `meteo`.

A simplified structure of the project is:

```text
project/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── meteo/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── admin.py
    │
    ├── templates/
    │   └── meteo/
    │       ├── layout.html
    │       ├── index.html
    │       ├── resorts.html
    │       └── summits.html
    │
    ├── static/
    │   └── meteo/
    │       ├── styles.css
    │       └── ...
    │
    └── fixtures/
        └── summits.json
```

The exact structure may change as the project is still being developed.

---

## Models

### Resort

The `Resort` model stores information about ski resorts.

Example fields:

```python
class Resort(models.Model):
    name = models.CharField(max_length=64)
    latitude = models.DecimalField(max_digits=10, decimal_places=2)
    longitude = models.DecimalField(max_digits=10, decimal_places=2)
    base_elevation = models.IntegerField()
    top_elevation = models.IntegerField()
    region = models.CharField(max_length=64)
    description = models.TextField()
```

### Summit

The `Summit` model stores information about important mountain summits.

Example fields:

```python
class Summit(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    top_elevation = models.IntegerField()
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lon = models.DecimalField(max_digits=10, decimal_places=6)
    region = models.CharField(max_length=64)
    description = models.TextField()
```

---

## Installation

To run this project locally, clone the repository and create a virtual environment.

```bash
git clone <repository-url>
cd <project-folder>
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

On macOS/Linux:

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Run the development server:

```bash
python manage.py runserver
```

Then open the local server in your browser:

```text
http://127.0.0.1:8000/
```

---

## Loading initial data

Some data can be loaded automatically using Django fixtures.

For example, if summit data is stored in:

```text
meteo/fixtures/summits.json
```

It can be loaded with:

```bash
python manage.py loaddata summits
```

If resort data is also stored in a fixture, it can be loaded in the same way:

```bash
python manage.py loaddata resorts
```

---

## Weather data

The project uses the Open-Meteo API to retrieve weather information.

The goal is to display weather values for both the base and top elevation of each resort, including:

- Temperature
- Snowfall
- Current or nearest-hour weather conditions

This part of the project is still being improved.

---

## Responsive design

The layout is designed to work on both desktop and mobile devices.

On desktop:

- Resort or summit cards appear in side columns
- The map appears in the center

On mobile:

- The map appears first
- Cards are displayed below
- The map height is adjusted for smaller screens

---

## Current development status

This project is not completely finished yet.

Completed or mostly completed:

- Django project setup
- Basic models
- Ski resort page
- Leaflet map integration
- Resort markers
- Card-marker interaction
- Basic responsive layout
- Initial weather API integration

Still in progress:

- Main summits page
- Final summit descriptions
- Weather display improvements
- Better styling and UI details
- More complete fixtures
- Final testing
- Final CS50W project documentation and video preparation

---

## Possible future improvements

Some improvements that could be added later:

- Add detailed pages for each resort and summit
- Add snow depth and forecast charts
- Add weather icons
- Improve mobile design
- Add filters by region or elevation
- Add hiking or skiing difficulty information
- Add saved favorite resorts or summits
- Add error handling when the weather API is unavailable
- Deploy the project online

---

## Author

Created by Aitana Cruxent as part of the CS50W Final Project.

---

## Acknowledgements

This project uses:

- [Django](https://www.djangoproject.com/)
- [Leaflet](https://leafletjs.com/)
- [OpenStreetMap](https://www.openstreetmap.org/)
- [Open-Meteo](https://open-meteo.com/)
- [Bootstrap](https://getbootstrap.com/)

---

## Note

This README will be updated as the project continues to evolve.
