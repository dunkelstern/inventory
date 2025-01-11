## Small parts inventory management

This project is a small parts inventory management system. It is thought out to
be a flexible parts database which keeps all relevant information as well as
datasheets, prices and a visual representation where you stored the part.

The idea is that the system may tell you in which compartment of which box in
what area of your workshop you have to search for to find the part you
currently need. It has been optimized to store information for electronics
parts and small other hardware like screws, nuts and bolts.

### Prerequisites for manual install or docker Standalone

As configured by default you will need the following:

- A postgres database named `inventory` with a postgres user `inventory` that
  may connect without password or by default with the password `inventory`

### Installation (manual)

You will need:
- Python > 3.10
- Poetry to install requirements and create a virtualenv

This is a standard Django 5.1 application, if you know how to deploy those the
following might sound familiar:

1. Checkout repository:
   - Github `git clone https://github.com/dunkelstern/inventory.git`
   - ForgeJo: `git clone https://git.dunkelstern.de/dunkelstern/inventory.git`
2. Change to checkout: `cd inventory`
3. Install virtualenv and dependencies:
   ```
   poetry install --no-root
   ```
4. If you want to use the system in another language than the default english set it
   up in the `inventory_project/settings.py`:
   ```python
   LANGUAGE_CODE = 'en-us' # or something like 'de-de'
   ```
   see the settings file for defined languages.
5. If you changed the language rebuild the translation files:
   ```
   poetry run python manage.py compilemessages
   ```
6. Migrate the Database:
   ```
   poetry run python manage.py migrate
   ```
7. Optionally create an admin user. If not done manually the application will prompt you on first run.
   ```
   poetry run python manage.py createsuperuser
   ```
8. Run the server
  - Development server (not for deployment!): `poetry run python manage.py runserver`
  - Deployment via `gunicorn` on port 8000: `poetry run gunicorn inventory_project.wsgi -b 0.0.0.0:8000`

Then login on `http://localhost:8000/admin/` for the Django admin interface or
go to `http://localhost:8000` to enter the inventory management system directly

### Installation (Standalone Docker)

#### Building yourself

1. Checkout repository:
   - Github `git clone https://github.com/dunkelstern/inventory.git`
   - ForgeJo: `git clone https://git.dunkelstern.de/dunkelstern/inventory.git`
2. Change to checkout: `cd inventory`
3. Build Docker image: `docker build -t 'dunkelstern/inventory:latest' .`

next steps below

#### Pulling from docker hub

1. Pull Docker image: `docker pull 'dunkelstern/inventory:latest'`

next steps below

#### Next steps

1. Install a PostgreSQL DB somewhere and create a user and DB.
2. Setup environment (put everything in a `.env` file):
   ```
   INVENTORY_DB_HOST=
   INVENTORY_DB_NAME=
   INVENTORY_DB_USER=
   INVENTORY_DB_PASSWORD=

   INVENTORY_SECRET_KEY=
   INVENTORY_EXTERNAL_URL=http://localhost:8000
   INVENTORY_DEBUG=FALSE

   INVENTORY_LANGUAGE=en-us
   INVENTORY_TIMEZONE=UTC

   INVENTORY_PAGE_SIZE=25
   ```
3. Create a media directory for uploaded files: `mkdir -p media`
4. Run the container:
   ```
   docker run \
     --name inventory \
     -d \
     --restart=always \
     --env-file=.env \
     -p 8000:8000 \
     --volume ./media:/media \
     dunkelstern/inventory:latest 
   ```
5. The onboarding process will start on first call of the application and prompt to create an admin user.

### Installation (Docker compose)

1. Checkout repository:
   - Github `git clone https://github.com/dunkelstern/inventory.git`
   - ForgeJo: `git clone https://git.dunkelstern.de/dunkelstern/inventory.git`
2. Change to checkout: `cd inventory`
3. Copy `default.env` to `override.env` and check settings. Use a long random string for `INVENTORY_SECRET_KEY`!
4. Build the stack: `docker-compose up --build -d`
5. You can reach the application on port 8000
6. The onboarding process will start on first call of the application and prompt to create an admin user.

The compose stack will create two volumes:

- `inventory_dbdata` which contains the PostgreSQL database directory
- `inventory_mediafiles` which will contain any uploaded file

### Additional information

1. The initial DB migration pre-populates the database with some useful defaults
  and some pre-defined distributors and form-factors usable for electronics
  inventories as well as a "Default Workshop" to be able to navigate everything.
2. For editing parts the Django admin interface is used, so edit-links will only
  appear if the currently logged in user is a `staff` user (set the checkbox
  in the admin area).
3. If you want to change the default number of items on paginated views you can
  set the page size in the settings by providing a parameter `PAGE_SIZE`
4. If you want to run this as a systemd service see the
  [the service file](inventory.service) in the root of this repository for an
  example.

### Changelog

#### 1.1

- Part count can be configured to be available in settings
- Currency can be configured in settings
- Complete system is translateable (English and German are provided)

![Settings](docs/settings.jpeg)

### Screenshots

#### Login

To be able to list all parts you'll need to login. You basically have three
levels of permissions:

- Normal Users
- Staff Users
- Admin Users

Normal users can view all parts and search, Staff users may edit in addition.
Admin users can create Users and do everything (like adding new layouts, etc.).

![Login page](docs/login.jpeg)

#### Overview Page

here we have a layer of containers, you may nest multiple containers into each
other, for example to define a cupboard which contains multiple boxes of parts,
or multiple rooms in your workshop that contain cupboards, etc.

![Overview](docs/main_area.jpeg)

#### Box View

This is a container that contains parts. You may define your layouts (number of
compartments, number of items per compartment and layout of compartments
themselves) all by yourself in the admin backend, by default the database comes
with an assortment of Ikea and Raaco sorter boxes.

![Box view 1](docs/smd_box.jpeg)

![Box view 2](docs/smd_box_marker.jpeg)

The Overview and Box views are designed to be used on a touch-screen and the HTML,
CSS and Javascript are designed to work on older Hardware (Apple iOS 9 has been
tested at lowest, so this works from iPad 2 up to the newest pro).

#### Part detail view

This is the detail view of a part, this is useful to find all parts by manufacturer
or distributor, or when a part has multiple datasheets.

![Detail view](docs/part.jpeg)

#### Part edit view

Editing is done on the standard Django admin interface, so all users that have no
*staff* privileges only can view all parts, all with *staff* privileges have access
to the django admin backend and can edit parts too.

![Edit view](docs/edit_part.jpeg)

#### Search function

If you click on the loupe symbol on top you'll get a popup searchbox for a fulltext
search through all parts.

![Search view](docs/search.jpeg)

The search results contain a link to the container the object is stored in and if
you click that link the compartment will be hilighted so you can find the part faster:

![Search view hilight](docs/search_hilight.jpeg)

You can also reach the first datasheet directly from the search results by clicking
on the icon in front of the description text.

#### Tag cloud

If you select the tag icon in the header bar you will get a dynamically searchable
tag cloud if you do not know a search term exactly or if you need a group of parts
(e.g. give me all transistors of any type).

![Tag cloud](docs/tags.jpeg)

The detail view of a tag will list all items with that tag, as well as all containers
or footprints that have been assigned this tag:

![Tag detail](docs/tag_detail.jpeg)

Editing is in Django backend:

![Tag editing](docs/edit_tag.jpeg)

#### Other options

You can browse your parts inventory by distributor or part manufacturer if you want:

![Manufacturer list](docs/manufacturer.jpeg)

![Manufacturer detail](docs/manufacturer_detail.jpeg)

![Manufacturer edit](docs/edit_manufacturer.jpeg)

The distributor views have a convenient search box if a parametrized search link has
been set up in the backend.

This link will be used to link to a part directly if a part has a distributor part
number saved.

![Distributor list](docs/distributor.jpeg)

![Distributor detail](docs/distributor_detail.jpeg)

![Distributor edit](docs/edit_distributor.jpeg)
