from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user
from app.models.user import User
from app.db.session import get_db
from app.schemas.user import UserCreate, UserResponse, UserLogin 
from app.services import auth_service


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db),
):
    return auth_service.register_user(
        db=db,
        username=user_data.username,
        email=user_data.email,
        password=user_data.password,
    )

@router.post("/login")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db),
):
    return auth_service.login_user(
        db=db,
        username=user_data.username,
        password=user_data.password,
    )

@router.get("/me", response_model=UserResponse)
def get_me(
    current_user: User = Depends(get_current_user),
):
    return current_user