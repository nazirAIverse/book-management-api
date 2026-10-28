from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.book import BookCreate, BookResponse, BookUpdate
from app.services import book_service


router = APIRouter(
    prefix="/books",
    tags=["Books"],
)


@router.get("/", response_model=list[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return book_service.get_all_books(db)


@router.post(
    "/",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    book_data: BookCreate,
    db: Session = Depends(get_db),
):
    return book_service.create_book(
        db=db,
        title=book_data.title,
        author=book_data.author,
        year=book_data.year,
    )


@router.get("/{book_id}", response_model=BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    return book_service.get_book_or_404(db, book_id)


@router.put("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book_data: BookUpdate,
    db: Session = Depends(get_db),
):
    return book_service.update_book(
        db=db,
        book_id=book_id,
        title=book_data.title,
        author=book_data.author,
        year=book_data.year,
    )


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book_service.delete_book(db, book_id)
    return None