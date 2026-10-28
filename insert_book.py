
from app.db.session import SessionLocal
from app.models.book import Book

db = SessionLocal()

try:
    book = Book(
        title="The Hobbit",
        author="J.R.R. Tolkien",
        year=1937,
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    print(book.id)
    print(book.title)

finally:
    db.close()
