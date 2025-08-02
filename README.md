# alx_travel_app_0x00

A travel listing API built with Django and Django REST Framework.

## Features

- Listings: Create and browse travel properties.
- Bookings: Reserve listings with check-in/out dates.
- Reviews: Rate and comment on listings.
- Swagger API Docs at `/swagger/`
- MySQL database configured via `django-environ`.

## Setup

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed
python manage.py runserver
