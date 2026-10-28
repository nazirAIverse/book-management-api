from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.repositories import user_repository


def register_user(
    db: Session,
    username: str,
    email: str,
    password: str,
):
    existing_username = user_repository.get_user_by_username(
        db, username
    )

    if existing_username is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username already registered",
        )

    existing_email = user_repository.get_user_by_email(
        db, email
    )

    if existing_email is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered",
        )

    hashed_password = hash_password(password)

    return user_repository.create_user(
        db=db,
        username=username,
        email=email,
        hashed_password=hashed_password,
    )