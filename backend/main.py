from __future__ import annotations

import json
from datetime import UTC, datetime
from pathlib import Path
from typing import List

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = Path("/app/data") if Path("/app").exists() else BASE_DIR.parent / "data"
BOOKS_FILE = DATA_DIR / "books.json"


def current_timestamp() -> str:
    return datetime.now(UTC).isoformat()


def default_books() -> list[dict]:
    timestamp = current_timestamp()
    return [
        {
            "id": 1,
            "title": "Война и мир",
            "author": "Лев Толстой",
            "description": "Роман-эпопея о судьбах людей на фоне исторических событий начала XIX века.",
            "publisher": "Эксмо",
            "year": 2022,
            "category": "Художественная литература",
            "available": True,
            "created_at": timestamp,
        },
        {
            "id": 2,
            "title": "Python для сложных задач",
            "author": "Лучано Рамальо",
            "description": "Практическое руководство по современным возможностям Python.",
            "publisher": "Питер",
            "year": 2023,
            "category": "Программирование",
            "available": True,
            "created_at": timestamp,
        },
        {
            "id": 3,
            "title": "Архипелаг ГУЛАГ",
            "author": "Александр Солженицын",
            "description": "Документально-художественное исследование репрессивной системы СССР.",
            "publisher": "АСТ",
            "year": 2021,
            "category": "История",
            "available": False,
            "created_at": timestamp,
        },
    ]


def ensure_books_file() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if not BOOKS_FILE.exists():
        BOOKS_FILE.write_text(
            json.dumps(default_books(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )


def load_books() -> list[dict]:
    ensure_books_file()
    return json.loads(BOOKS_FILE.read_text(encoding="utf-8"))


def save_books(books: list[dict]) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    BOOKS_FILE.write_text(
        json.dumps(books, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    publisher: str
    year: int
    category: str
    available: bool
    created_at: str


class BookCreate(BaseModel):
    title: str = Field(..., min_length=1)
    author: str = Field(..., min_length=1)
    description: str = Field(..., min_length=1)
    publisher: str = Field(..., min_length=1)
    year: int
    category: str = Field(..., min_length=1)
    available: bool = True


app = FastAPI(title="ElectoLibrary API")


@app.on_event("startup")
def startup() -> None:
    ensure_books_file()


@app.get("/api/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/books", response_model=List[Book])
def get_books() -> list[dict]:
    return load_books()


@app.post("/api/books", response_model=Book, status_code=201)
def create_book(payload: BookCreate) -> dict:
    books = load_books()
    next_id = max((book["id"] for book in books), default=0) + 1

    new_book = {
        "id": next_id,
        "title": payload.title,
        "author": payload.author,
        "description": payload.description,
        "publisher": payload.publisher,
        "year": payload.year,
        "category": payload.category,
        "available": payload.available,
        "created_at": current_timestamp(),
    }

    books.append(new_book)
    save_books(books)
    return new_book


@app.delete("/api/books/{book_id}")
def delete_book(book_id: int) -> dict[str, int]:
    books = load_books()
    updated_books = [book for book in books if book["id"] != book_id]

    if len(updated_books) == len(books):
        raise HTTPException(status_code=404, detail="Book not found")

    save_books(updated_books)
    return {"deleted_id": book_id}
