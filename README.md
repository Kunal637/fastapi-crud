# FastAPI CRUD App

Small FastAPI example implementing basic CRUD for users using an in-memory store.

Project layout

- `app/` - FastAPI application package
  - `main.py` - application entry
  - `routes/users.py` - CRUD routes
  - `schemas.py` - Pydantic models
  - `requirements.txt` - Python deps
  - `Dockerfile` - container image

Requirements

- Python 3.12
- Docker (optional)

Install and run locally

1. From project root install dependencies:

```bash
pip install -r app/requirements.txt
```

2. Start the dev server (from project root):

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Run with Docker

1. Build the image (from project root):

```bash
docker build -t fastapi-crud -f app/Dockerfile .
```

2. Run container:

```bash
docker run -p 8000:8000 fastapi-crud
```

API

Base URL: http://localhost:8000

Endpoints

- POST /users
  - Create a user
  - Body: { "name": "Alice", "age": 30 }
  - Response: { "id": 1, "name": "Alice", "age": 30 }

- GET /users
  - List all users
  - Response: [ { "id": 1, "name": "Alice", "age": 30 }, ... ]

- GET /users/{user_id}
  - Get single user
  - Returns 404 if not found

- PUT /users/{user_id}
  - Update user data
  - Body same as POST

- DELETE /users/{user_id}
  - Delete user
  - Returns a simple confirmation message

Notes

- This project uses an in-memory dict as the data store. Restarting the server will clear data.
- Schemas use Pydantic v2 style (`model_config = {"from_attributes": True}`) in `app/schemas.py`.

License

- Public domain / learnings. Use freely.
