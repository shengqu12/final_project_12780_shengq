## Community Climate Dashboard
This is about a dashboard showing the risk level of different borough in New York City in 2024. With this html, the decision makers can pick and compare different months in 2024 to decide which community needs more aids from government to deal with climate problem.

# ERD

![ERD diagram](./images/ERD%20.png)

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
