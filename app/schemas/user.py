from typing import Optional
from pydantic import BaseModel, EmailStr


# 공통 스키마
class UserBase(BaseModel):
    email: str
    name: str


# 회원가입 (Request)
class UserCreate(BaseModel):
    email: EmailStr
    name: str
    uid: str


# 로그인 (Request)
class UserLogin(BaseModel):
    uid: str


# 회원 정보 수정 (Request)
class UserUpdate(BaseModel):
    name: Optional[str] = None


# 회원 정보 조회 (Response)
class UserRead(UserBase):
    id: int

    class Config:
        from_attributes = True


# 토큰 발급 (Response)
class TokenRefresh(BaseModel):
    refresh_token: str


# 토큰 발급 (Response)
class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
