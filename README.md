# Medication Adherence API

A backend API for managing medications, built with FastAPI, PostgreSQL, and SQLAlchemy.  
This project supports full CRUD operations for medication records and demonstrates clean backend structure with routers, schemas, models, and database integration.

## Features

- Create medications
- View all medications
- Update medications
- Delete medications
- PostgreSQL database integration
- FastAPI interactive documentation
- Structured project architecture using routers, schemas, and models

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Uvicorn
- python-dotenv

## Project Structure

```text
med-adherence-system/
├── .venv/
├── .env
├── main.py
├── database.py
├── models.py
├── schemas.py
├── README.md
└── routers/
    ├── __init__.py
    └── medications.py