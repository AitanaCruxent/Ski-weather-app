# PiriNeu

PiriNeu is a Django web application created as my final project for CS50W. The project is a mountain weather and route-oriented web application focused on the Catalan Pyrenees and snow activites. At the moment, it only gives detailed information about snow prediction and temperature. Its main goal is to bring together useful information for people who ski, or spend time in the Catalan mountains during winter. The application currently includes weather-focused pages for ski resorts, a section for main summits, an avalanche-risk information page, and a personal route-saving feature for authenticated users. 

This project started from a simple idea: I wanted to build something useful and connected to a real interest of mine. I am a huge fan of mountain sports and in particular winter sports as skiing and backcountry skiing. Catalunya has many ski resorts and mountain areas, and many websites provide usefull information, but there is one thing I miss during winter season: somewhere to see the snow prediction for all the important points of the country at a glance. Therefore, I created a web app that helps you decide where to go depending on the snow prediction and you can check several points in the map at the same time.

About the naming, Pirineu is Pyernees in Catalan and Neu is snow, so I combined the two words creating PiriNeu to make emphasis that this web application is centered in snow weather and snow activities, for now.

The project is still a first version. Some parts are already functional, while other parts are intentionally left as future improvements. My long-term idea would be to make this into a more complete winter mountain companion app, where users could share weather info in real time to inform the rest of the users, save routes, organize their mountain activities and consult more detailed weather information.  For this submission, I focused on building a solid Django application with multiple models, user authentication, interactive pages, external real-time information, and responsive design.

---

## Distinctiveness and Complexity

I believe this project satisfies the distinctiveness requirement because it is not a copy of any of the previous CS50W projects. It is not an e-commerce site, not a mail client, not a wiki, and not a generic social network. Instead, it is a domain-specific web application focused on mountain weather and Pyrenean outdoor activity. The application combines several different types of functionality: public informational pages, interactive maps, weather-related content, external embedded data, and private user-generated content.

The project is distinctive because its structure and purpose are built around a specific real-world use case. A user visiting PiriNeu is not simply browsing posts or buying products; they are checking information about ski resorts, summits, avalanche conditions, and their own saved routes. The project required me to think about how to represent real mountain locations in the database, how to organize the information visually, and how to make navigation between pages intuitive. 

The complexity of the project comes from combining several moving parts. The application uses Django models to store structured information about ski resorts, summits, and user routes. It also uses Django authentication to provide acces to using the different app features. For example, for “My Routes”, each user can save and delete content, which means that the application must not only create and display database objects, but also ensure that users only see and manage their own data.

Another important part of the project’s complexity is the front-end interaction. The project uses custom HTML, CSS, JavaScript, Bootstrap, and Leaflet maps. On the ski resorts and summits pages, the layout is not just a static list of information. Cards and maps are designed to work together visually, and the interface includes responsive styling so that the pages remain usable on smaller screens. I spent time improving the navigation bar, the home page, the cards, and the general visual identity of the site so that it feels like a coherent application rather than a collection of separate Django templates.

The application also includes real-time or external information. The ski resort and summit sections were designed around weather information provided by Open-Meteo API, and the avalanche bulletin page embeds information from the official catalan avalanche danger source, ICGC. This required thinking about how to display information that is not only stored in my database, but also obtained or shown from external services. Even though this first version does not yet include every weather detail I would like, the architecture and design of the project are already oriented toward displaying useful mountain conditions.

To conclude, the project includes the combination of several features that make this web app more complex than the projects during the course. It has a public/private page structure, multiple related content areas, authenticated user data, interactive UI behavior, external embedded content, custom responsive design, and a clear future development path. The current version is intentionally focused and manageable, but it is built in a way that could be extended with more detailed forecasts, favorite routes, saved lists, richer user profiles, and additional mountain safety information.

---

## Current Features

### Home Page

The home page introduces the application and gives users a general overview of what they can do. The design changes depending on whether the user is authenticated or not. The public version presents the idea of the project and encourages the user to log in or register. The authenticated version gives easier access to the main sections of the application and a list of the routes shared during the last week ordered by the date they were completed.

### Ski Resorts

For only authenticated users, the ski resorts page displays the ski resorts in Catalunya. Each resort is represented with information such as its name, location, top and base elevation, and snow and temperature details. The page also includes an interactive map, which makes the data easier to understand visually.

The ski resorts included in the project are focused on Catalunya and the Pyrenees. Examples include La Molina, Masella, Baqueira Beret, Boí Taüll, Espot, Port Ainé, Vall de Núria, Vallter, and Port del Comte.

### Main Summits

For only authenticated users, the summits page focuses on important mountains in Catalunya and the Catalan Pyrenees. The idea of this section is to provide useful information for people interested in preparing a backcountry route or checking weather in high mountain areas.

The database includes summits such as Pica d’Estats, Pedraforca, Puigpedrós, Bastiments, Montardo, Tossa Plana de Lles, Pic de Certascan, and others.

### Avalanche Bulletin

For only authenticated users, the avalanche bulletin page displays updated avalanche danger information from an official external source. I included this because avalanche danger is an important part of mountain safety, especially in winter and spring conditions. Instead of manually copying this information, the project embeds the external ICGC (Institut Cartogràfic i Geològic de Catalunya) bulletin so that users can consult the original up-to-date source from within the application.

### My Routes

The “My Routes” section allows users to save personal mountain routes. A user can create a route with information such as name, location, distance, duration, date completed, and weather notes.

This section is private: each route is connected to the user who created it. Users should only see their own saved routes. This was an important part of the project because it required using Django’s authentication system together with user-specific database filtering.

---

## Future Improvements

This submission represents the first version of PiriNeu. There are several features I would like to add in the future.

One important improvement would be to create a more complete saved routes system. At the moment, users can save personal routes, but I would like to expand this into a richer route list where users can edit routes, mark favorites, add difficulty levels, upload photos, and maybe filter routes by location, season, or type of activity.

Another future improvement would be to add more detailed weather information. I would like to display forecasts in a clearer and more complete way, possibly including hourly temperature, snowfall and wind in a more detailed card or page with detailed information. 

I would also like to improve the design and user experience. The current version already has a custom layout, but future work could include better mobile navigation, more consistent card styling, loading states, map improvements, and more accessible design.

Finally, I would like to deploy the project online with a production database. This would require moving from the current local SQLite development setup to a hosted environment, configuring static files correctly, and possibly using a production-ready database such as PostgreSQL.

---

## Files and Project Structure

The exact project structure may vary slightly, but the main files I created or edited are described below.

### `manage.py`

This is the standard Django management file. It is used to run development commands such as starting the server, applying migrations, creating a superuser, and loading fixture data.

### Project settings folder

This folder contains the main Django configuration files.

#### `settings.py`

This file contains the project configuration, including installed apps, middleware, templates, static files, database settings, and authentication settings. The project currently uses SQLite for local development.

#### `urls.py`

This file connects the main project URLs to the application URLs. It includes the routes that allow the browser to access the different pages of the site.

### `meteo/models.py`

This file contains the database models used by the application.

The main models include:

- A model for ski resorts
- A model for summits
- A model for user routes

The route model is connected to Django’s `User` model so that each route belongs to the user who created it. This is what makes the “My Routes” section private and user-specific.

### `meteo/views.py`

This file contains the logic for rendering pages and handling form submissions. It includes views for the home page, ski resorts page, summits page, avalanche bulletin page, authentication-related navigation, and the personal routes section.

The route-related views handle creating and deleting user routes, checking required form fields, saving data to the database, and displaying success or error messages.

### `meteo/urls.py`

This file defines the URL patterns for the `meteo` app. It maps specific URLs to the corresponding view functions.

### `meteo/admin.py`

This file registers the project models in the Django admin interface. This makes it possible to manage resorts, summits, and routes through the Django admin panel during development.

### `meteo/templates/meteo/layout.html`

This is the base template used by the site. It contains the shared HTML structure, including the header, navigation bar, static files, and template blocks used by other pages.

### `meteo/templates/meteo/index.html`

This is the home page template. It presents the project and gives users access to the main sections of the application.

### `meteo/templates/meteo/skiresorts.html`

This template displays the ski resorts page. It contains the layout for resort cards and the Leaflet map.

### `meteo/templates/meteo/summits.html`

This template displays the main summits page. It is similar in concept to the ski resorts page but focused on mountain summits.

### `meteo/templates/meteo/bpa.html`

This template displays the avalanche bulletin page. It embeds avalanche danger information from an external official source.

### `meteo/templates/meteo/myroutes.html`

This template displays the user’s saved routes. It includes the form for adding a new route and the cards that show previously saved routes.

### `meteo/static/meteo/styles.css`

This file contains the custom CSS for the project. It defines the layout, colors, navigation bar, cards, forms, route section, map size, responsive behavior, and general visual identity of the site.

### `fixtures/`

The fixtures folder contains JSON data that can be loaded into the database automatically. This is useful for adding ski resorts or summits without manually entering each object through the admin panel.

### `requirements.txt`

This file contains the Python packages required to run the project.

At the moment, the project uses Django and its dependencies:

```txt
asgiref==3.11.0
Django==6.0.1
sqlparse==0.5.5
```

No extra Python packages are required for Leaflet or Bootstrap because those are used through front-end files or CDN links.

---

## How to Run the Application

First, clone the repository:

```bash
git clone <repository-url>
cd <project-folder>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

On Windows:

```bash
venv\Scripts\activate
```

On macOS or Linux:

```bash
source venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

If fixture data is included, load it with:

```bash
python manage.py loaddata <fixture-name>
```

For example:

```bash
python manage.py loaddata summits
```

Create a superuser if you want to use the admin panel:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Then open the application in the browser at:

```text
http://127.0.0.1:8000/
```

---

## Author

Created by Aitana Cruxent as the final project for CS50W.

---

## Acknowledgements

This project uses the following technologies and services:

- Django
- Python
- HTML
- CSS
- JavaScript
- Bootstrap
- Leaflet
- OpenStreetMap
- Open-Meteo
- Official avalanche bulletin information from ICGC