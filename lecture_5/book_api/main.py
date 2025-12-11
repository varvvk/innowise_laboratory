from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from .database import create_db, SessionLocal
from .models import BookOrm
from .schemas import BookCreate, BookResponse


app = FastAPI()

create_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/books/", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    db_book = BookOrm(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


@app.get("/books/", response_model=List[BookResponse], status_code=status.HTTP_200_OK)
def get_book(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    books = db.query(BookOrm).offset(skip).limit(limit).all()

    return books


@app.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    db_book = db.query(BookOrm).filter(BookOrm.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(db_book)
    db.commit()

    return {"detail": "Book deleted"}


@app.put("/books/{book_id}", response_model=BookResponse)
def update_book(book_id: int, new_data: BookCreate, db: Session = Depends(get_db)):
    book = db.query(BookOrm).filter(BookOrm.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    book.title = new_data.title
    book.author = new_data.author
    book.year = new_data.year

    db.commit()
    db.refresh(book)

    return book


@app.get("/books/search/", response_model=List[BookResponse])
def search_books(
    title: Optional[str] = Query(None),
    author: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    query = db.query(BookOrm)

    if title:
        query = query.filter(BookOrm.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(BookOrm.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(BookOrm.year == year)

    books = query.offset(skip).limit(limit).all()

    return books
