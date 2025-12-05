from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserRead,
    UserUpdate,
)
from app.services.user_service import register_user_service, update_user_service

router = APIRouter()


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_user(request: UserCreate, db: Session = Depends(get_db)):
    """회원가입 API"""
    created_user = register_user_service(db, request)
    return created_user


@router.put("/", response_model=UserRead, status_code=status.HTTP_200_OK)
def update_user(
    request: UserUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """회원 정보 수정"""
    updated_user = update_user_service(db, current_user, request)
    return updated_user


@router.get("/me", response_model=UserRead, status_code=status.HTTP_200_OK)
def get_me(current_user: User = Depends(get_current_user)):
    """회원 정보 조회"""
    return current_user


# @router.get("/")
# def register(request: UserCreate, db=Depends(get_db)):
#     """회원 정보 조회"""
#     return register_user(db, request)


# @router.put("/me", response_model=UserRead)
# def get_me(current_user=Depends(get_current_user)):
#     """회원 정보 업데이트"""
#     return current_user


# @router.post("/me/deletion", response_model=UserRead)
# def get_me(current_user=Depends(get_current_user)):
#     """회원 탈퇴 요청"""
#     return current_user


# @router.delete("/me/deletion", response_model=UserRead)
# def get_me(current_user=Depends(get_current_user)):
#     """회원 탈퇴 철회"""
#     return current_user
