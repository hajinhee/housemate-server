from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.user import (
    TokenRefresh,
    TokenResponse,
    UserLogin,
)
from app.services.user_service import (
    login_user_service,
    refresh_token_service,
)
from app.utils.jwt_handeler import create_access_token, verify_token

router = APIRouter()


@router.post("/login", response_model=TokenResponse, status_code=status.HTTP_200_OK)
def login_user(request: UserLogin, db: Session = Depends(get_db)):
    """회원 로그인 API"""
    tokens = login_user_service(db, request)
    return tokens


@router.post(
    "/token/refresh", response_model=TokenResponse, status_code=status.HTTP_200_OK
)
def refresh_token(request: TokenRefresh):
    """access, refresh 토큰 재발급 API"""
    tokens = refresh_token_service(request)
    return tokens
