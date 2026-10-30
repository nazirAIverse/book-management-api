from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.core.security import hash_password
from app.core.security import verify_password, create_access_token
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

def login_user(
    db: Session,
    username: str,
    password: str,
):
    user = user_repository.get_user_by_username(db, username)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    if not verify_password(password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    access_token = create_access_token(
        data={"sub": str(user.id)}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }