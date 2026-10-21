# TempBox 📦

**TempBox** is a REST API for creating and storing temporary notes. It allows users to create notes with a limited lifetime, retrieve them using a unique key, and delete them manually.

This project was built to practice Python, FastAPI, and Redis.

## Features

- Create notes with unique keys.
- Retrieve notes by key.
- Automatically expire notes after a specified time-to-live (TTL).
- Manually delete notes.
- Validate input data using Pydantic.
- Handle errors with appropriate HTTP status codes.
- Store data in Redis.

## Tech Stack

- **Python** — programming language.
- **FastAPI** — REST API framework.
- **Pydantic** — data validation.
- **Redis** — note storage and expiration management.
- **Docker Compose** — run Redis locally.

## Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd TempBox
```

### 2. Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

If the project includes a `requirements.txt` file, install the dependencies with:

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example` and configure the required environment variables.

Example configuration for local development:

```env
REDIS_URL=redis://localhost:6379/0
TEST_REDIS_URL=redis://localhost:6379/15
```

- `REDIS_URL` is used by the application to connect to Redis.
- `TEST_REDIS_URL` is intended for the test database.

Do not commit your `.env` file to the repository.

### 5. Start Redis

Make sure Docker is running, then execute:

```bash
docker compose up -d redis
```

### 6. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation (Swagger UI):

`http://127.0.0.1:8000/docs`

## API Endpoints

### Create a note

`POST /notes`

Example request:

```json
{
  "text": "Hello from TempBox!",
  "ttl_seconds": 300
}
```

Creates a note that expires after 300 seconds.

**Validation rules:**
- `text` — between 1 and 1000 characters.
- `ttl_seconds` — between 1 and 86400 seconds.

Example response — `201 Created`:

```json
{
  "key": "unique_key",
  "ttl_seconds": 300
}
```

### Retrieve a note

`GET /notes/{key}`

Returns the note's text, key, and remaining time-to-live.

Example response — `200 OK`:

```json
{
  "key": "unique_key",
  "text": "Hello from TempBox!",
  "ttl_seconds": 297
}
```

If the note does not exist or has expired, the API returns `404 Not Found`.

### Delete a note

`DELETE /notes/{key}`

Deletes a note using its key.

Successful response — `204 No Content`.

If the note does not exist, the API returns `404 Not Found`.

## Error Handling

- `404 Not Found` — the note does not exist or has expired.
- `422 Unprocessable Entity` — the request data failed validation.

## Project Structure

```text
TempBox/
├── app/
│   ├── routes/
│   │   └── note_router.py
│   ├── services/
│   │   └── note_service.py
│   ├── config.py
│   ├── exceptions.py
│   ├── redis_client.py
│   └── schemas.py
├── tests/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── main.py
└── README.md
```

## Project Goals

TempBox is a learning project focused on REST API development with FastAPI, Redis data storage, key expiration using TTL, input validation, and clean Python application structure.

