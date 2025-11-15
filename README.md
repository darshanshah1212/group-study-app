# Group Study App (grp_stdy)

A small Django-based group study app that uses WebSockets/Channels for real-time group interactions (chat/rooms). This repository contains the Django project (ASGI-ready) and a `core` app with consumers, routing, models, and templates.

## Quick overview

- Project: Group Study App
- Purpose: Real-time group study / chat using Django and WebSockets (Channels/ASGI)
- Main tech: Python, Django, Django Channels (ASGI), WebSockets
- Entry points: `manage.py`, `grp_stdy/asgi.py`, `core/consumers.py`

## Contents

- `manage.py` — Django CLI entry
- `grp_stdy/` — Django project settings and ASGI app
- `core/` — main app (consumers, routing, models, views, templates)
- `templates/index.html` — basic frontend
- `db.sqlite3` — local SQLite DB (add to .gitignore before pushing)

## Features

- Real-time WebSocket communication (group study rooms)
- Minimal frontend to demonstrate WebSocket connections
- ASGI configuration ready (`asgi.py`)

## Minimal contract (inputs / outputs)

- Inputs: WebSocket messages from clients (JSON/text) describing chat or room actions.
- Outputs: Broadcast messages to group room members.
- Error modes: connection failures, invalid messages — handled by consumer logic (see `core/consumers.py`).

## Prerequisites

- Python 3.8+ (3.10/3.11 recommended)
- pip
- (Optional) virtualenv or venv
- (Optional) `daphne` or an ASGI server for production

## Setup (local development)

1. Create and activate a virtual environment:

```powershell
# from project root (PowerShell)
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Install dependencies (add them to `requirements.txt` for later):

```powershell
pip install -r requirements.txt
# If you don't have requirements.txt yet, install Django and channels:
pip install django channels
```

3. Environment variables — recommended (do not commit secrets):

- `DJANGO_SECRET_KEY` (or set `SECRET_KEY` in a secure settings mechanism)
- `DEBUG=False` for production

4. Prepare database and run migrations:

```powershell
python manage.py migrate
python manage.py createsuperuser  # optional for admin access
```

5. Run the development server (ASGI):

```powershell
python manage.py runserver
# or use daphne for ASGI in dev:
# daphne -b 0.0.0.0 -p 8000 grp_stdy.asgi:application
```

Then open `http://127.0.0.1:8000/` and test the WebSocket functionality from the provided `index.html`.

## Testing

Add unit tests under `core/tests.py`. Run tests with:

```powershell
python manage.py test
```

## Preparing for GitHub — recommended pre-push cleanups

1. Add a `.gitignore` that at minimum ignores:

- `__pycache__/`
- `.venv/` or `venv/`
- `db.sqlite3`
- `.env` or any file with secrets
- `.pyc` files

You can use a standard Python `.gitignore` (GitHub provides one when creating a repo).

2. Make sure you haven't committed secrets (search for `SECRET_KEY` in repo). Remove or rotate if present.

## GitHub: Recommended repo name, description, and topics

- Suggested repo name: `group-study-app` or `grp_stdy`
- Short description (one line): "Django group study app with real-time WebSocket rooms (Django Channels)."
- Topics (tags): `django`, `channels`, `websockets`, `asgi`, `python`, `realtime`

## How to add this project to GitHub (PowerShell commands)

If this folder is not a git repo yet:

```powershell
# initialize repo (if not already initialized)
git init
git add .
git commit -m "Initial commit: add Group Study App"
git branch -M main
```

Create a remote repository on GitHub using the web UI (recommended) or with the GitHub CLI (`gh`) as shown below.

### Push using the GitHub web UI (classic flow)

1. Go to https://github.com/new
2. Repository name: `group-study-app` (or your chosen name)
3. Description: "Django group study app with real-time WebSocket rooms (Django Channels)."
4. Choose Public or Private
5. Do NOT select "Initialize this repository with a README" if you already created one locally (avoid duplicate README merge) — if you did, you can pull first.
6. Click Create repository

After GitHub creates the repo, it will give you remote commands. Run (replace `<URL>` with the repo URL):

```powershell
git remote add origin <URL>
git push -u origin main
```

### Push using GitHub CLI (`gh`) — optional

If you have `gh` installed and authenticated:

```powershell
# from project root
gh repo create group-study-app --public --description "Django group study app with real-time WebSocket rooms (Django Channels)." --source=. --remote=origin --push
```

This creates the repo on GitHub, adds `origin`, and pushes the current branch.

## Recommended GitHub repository settings

- Add a license (MIT is common for small projects)
- Add topics/tags (see above)
- Add a short README summary (we already added) and longer README (this file)
- Add `.gitignore` (Python) if not present
- Protect `main` branch (require PR reviews) if this will be a collaborative repo
- Add repository secrets (if deploying or CI needs secrets): `DJANGO_SECRET_KEY`, `DATABASE_URL`, any cloud credentials

## Small, safe extras you can add now

- `LICENSE` (MIT)
- `CONTRIBUTING.md` with a short contribution guide
- `requirements.txt` (pin the versions you tested with)
- `.github/workflows/ci.yml` — basic GitHub Actions to run `python -m pip install -r requirements.txt` and `python manage.py test`

## Troubleshooting & notes

- If you see `sqlite` file changes and you don't want to push them, run `git rm --cached db.sqlite3` and add it to `.gitignore`.
- Confirm `SECRET_KEY` is never pushed. Use environment variables locally (e.g. a `.env` file kept out of git).

## Example PR / Contribution guidance

- Fork the repo (or create a branch), make changes, run tests locally, open a PR against `main`.
- Keep commits small and focused, include a test when adding behavior.

## License

Choose a license (MIT recommended for permissive open source). Add a `LICENSE` file with the chosen license text.

---

If you'd like, I can also:

- Add a `.gitignore` file tuned for Django
- Add a `requirements.txt` with versions
- Create a minimal GitHub Actions workflow to run tests on push/PR

Tell me which of those you'd like and I will add them next.

