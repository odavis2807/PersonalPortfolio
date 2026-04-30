# Personal Portfolio

A personal portfolio web application built with Django. Features a homepage, portfolio section, development journal, and an apps/games section.

---

## Tech Stack

- **Backend:** Django 4.2
- **Database:** PostgreSQL (SQLite in development)
- **Static files:** WhiteNoise
- **Testing:** pytest-django
- **Linting:** Ruff + Black
- **CI:** GitHub Actions

---

## Local Development Setup

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-name>
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements/base.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Open `.env` and fill in the required values. At minimum you need a `SECRET_KEY`.

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (for the admin panel)

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) — admin panel at [http://localhost:8000/admin](http://localhost:8000/admin).

---

## Running Tests

```bash
pytest
```

---

## Code Quality

```bash
ruff check .        # Lint
black --check .     # Check formatting
black .             # Auto-format
```

---

## Project Structure

```
├── config/               # Project settings, URLs, WSGI/ASGI
│   └── settings/
│       ├── base.py       # Shared settings
│       ├── development.py
│       └── production.py
├── templates/            # Global base templates
├── static/               # Global static files
├── requirements/
│   ├── base.txt
│   └── production.txt
└── manage.py
```

---

## Deployment

Set the following environment variables on your deployment platform:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Set to `False` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed domains |
| `DATABASE_URL` | Full PostgreSQL connection string |
| `DJANGO_SETTINGS_MODULE` | `config.settings.production` |

---

## Development Journal

This project is documented in the Dev section of the site itself, covering the full SDLC process, TDD approach, and decisions made along the way.
