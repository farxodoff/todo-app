# Todo App

A Django-based to-do web application with user authentication, CRUD operations, and PostgreSQL for production. Personal learning project — building it end-to-end from a bare Django skeleton to a deployed Ubuntu server.

## Features

### Implemented
- [x] Django 6.0.4 project scaffold
- [x] `tasks` app with `Task` model (owner, title, description, due date, importance, completion status, created_at)
- [x] Django admin integration with `list_display`, `list_filter`, `search_fields`
- [x] SQLite for local development
- [x] `.gitignore` and pinned `requirements.txt`

### Planned
- [ ] User sign-up / login / logout (built-in `django.contrib.auth`)
- [ ] Task CRUD views — list, create, edit, delete, toggle completion
- [ ] Bootstrap UI
- [ ] `.env`-based configuration (`django-environ`)
- [ ] PostgreSQL for production
- [ ] Deployment to Ubuntu 24.04 (gunicorn + nginx + systemd)
- [ ] Docker / docker-compose
- [ ] CI/CD with GitHub Actions

## Tech Stack

| Component     | Version / Choice                         |
|---------------|------------------------------------------|
| Python        | 3.12                                     |
| Django        | 6.0.4                                    |
| Database      | SQLite (dev), PostgreSQL (prod, planned) |
| Frontend      | Bootstrap (planned)                      |
| Deployment    | Ubuntu 24.04 (planned)                   |

## Quick Start (local dev)

> Commands assume Windows PowerShell. Substitute `source venv/bin/activate` on Linux/macOS.

```powershell
# 1. Clone the repo
git clone https://github.com/farxodoff/todo-app.git
cd todo-app

# 2. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. Create a superuser
python manage.py createsuperuser

# 6. Run dev server
python manage.py runserver
```

Open `http://127.0.0.1:8000/admin/` to access the admin panel and manage tasks.

## Project Structure

```
todo-app/
├── manage.py
├── requirements.txt
├── .gitignore
├── todoapp/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── tasks/                # Tasks application
    ├── models.py         # Task model
    ├── admin.py          # Admin registration
    ├── migrations/
    └── ...
```

## Task Model

| Field          | Type              | Notes                         |
|----------------|-------------------|-------------------------------|
| `owner`        | FK → `auth.User`  | `on_delete=CASCADE`           |
| `title`        | CharField(200)    | required                      |
| `description`  | TextField         | optional                      |
| `due_date`     | DateField         | optional                      |
| `is_important` | BooleanField      | default `False`               |
| `is_completed` | BooleanField      | default `False`               |
| `created_at`   | DateTimeField     | `auto_now_add=True`           |

Default ordering: uncompleted first → important first → due soonest → newest first.

## Status

Active development. See the "Planned" checklist above for the roadmap.
