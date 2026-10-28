from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.book import Book


def get_all_books(db: Session):
    statement = select(Book)
    return db.scalars(statement).all()


def get_book_by_id(db: Session, book_id: int):
    statement = select(Book).where(Book.id == book_id)
    return db.scalar(statement)


def create_book(db: Session, title: str, author: str, year: int | None):
    book = Book(
        title=title,
        author=author,
        year=year,
    )

    db.add(book)
    db.commit()
    db.refresh(book)

    return book


def update_book(
    db: Session,
    book: Book,
    title: str,
    author: str,
    year: int | None,
):
    book.title = title
    book.author = author
    book.year = year

    db.commit()
    db.refresh(book)

    return book


def delete_book(db: Session, book: Book):
    db.delete(book)
    db.commit()
    