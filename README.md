# Community Climate Dashboard

A Django web application to submit, visualize, and export community climate data.

## Features
- Data submission form
- Dashboard: Leaflet map charts
- Admin interface
- XLSX export
- Dockerized, with GitHub Actions CI and pytest-django tests

## Quick start (development)
1. git clone ...
2. python -m venv .venv; source .venv/bin/activate
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py runserver

Visit http://localhost:8000/dashboard/ to view the dashboard.
