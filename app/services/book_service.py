from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.repositories import book_repository


def get_book_or_404(db: Session, book_id: int):
    book = book_repository.get_book_by_id(db, book_id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )

    return book


def get_all_books(db: Session):
    return book_repository.get_all_books(db)


def create_book(
    db: Session,
    title: str,
    author: str,
    year: int | None,
):
    return book_repository.create_book(
        db=db,
        title=title,
        author=author,
        year=year,
    )


def update_book(
    db: Session,
    book_id: int,
    title: str,
    author: str,
    year: int | None,
):
    book = get_book_or_404(db, book_id)

    return book_repository.update_book(
        db=db,
        book=book,
        title=title,
        author=author,
        year=year,
    )


def delete_book(db: Session, book_id: int):
    book = get_book_or_404(db, book_id)
    book_repository.delete_book(db, book)