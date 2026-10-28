from sqlalchemy import select

from app.db.session import SessionLocal
from app.models.book import Book

db = SessionLocal()

try:
    statement = select(Book)
    books = db.scalars(statement).all()

    for book in books:
        print(book.id, book.title, book.author, book.year)

finally:
    db.close()
