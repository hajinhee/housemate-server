from fastapi import HTTPException, status
from passlib.context import CryptContext
from app.crud.user import (
    create_user,
    get_user_by_email,
    get_user_by_uid,
    update_user_name_by_id,
)
from app.schemas.user import TokenRefresh, UserCreate, UserLogin, UserUpdate
from app.utils.jwt_handeler import (
    create_access_token,
    create_refresh_token,
    verify_token,
)


def register_user_service(db, data: UserCreate):
    """회원 등록 서비스 로직"""
    # 사용자 조회
    existing_user = get_user_by_email(db, data.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="이미 가입된 이메일입니다."
        )
    created_user = create_user(db, data)
    return created_user


def update_user_service(db, user, data: UserUpdate):
    """회원 정보 수정 서비스 로직"""
    if not data.name:
        raise HTTPException(status_code=400, detail="수정할 이름이 없습니다.")

    updated_user = update_user_name_by_id(db, user.id, data.name)
    return updated_user


def login_user_service(db, data: UserLogin):
    """회원 로그인 서비스 로직"""
    # 사용자 조회
    existing_user = get_user_by_uid(db, data.uid)
    if not existing_user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="등록되지 않은 사용자입니다."
        )

    # access, refresh 토큰 생성
    access_token = create_access_token({"sub": str(existing_user.id)})
    refresh_token = create_refresh_token({"sub": str(existing_user.id)})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


def refresh_token_service(data: TokenRefresh):
    """리프레시 토큰 검증 후 새로운 엑세스 토큰 발급"""
    payload = verify_token(data.refresh_token)

    # 리프레시 토큰이 유효하지 않거나 만료된 경우
    if not payload or "error" in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="토큰이 유효하지 않거나 만료되었습니다. 다시 로그인해 주세요.",
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="토큰에 잘못된 데이터가 포함되어 있습니다.",
        )

    # access, refresh 토큰 생성
    access_token = create_access_token({"sub": str(user_id)})
    refresh_token = create_refresh_token({"sub": str(user_id)})

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }
