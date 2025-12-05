from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate


def get_user_by_email(db: Session, email: str):
    """이메일 조회 쿼리"""
    return db.query(User).filter(User.email == email).first()


def get_user_by_uid(db: Session, uid: str):
    """uid 조회 쿼리"""
    return db.query(User).filter(User.uid == uid).first()


def create_user(db: Session, data: UserCreate):
    """회원 등록 쿼리"""
    user = User(email=data.email, name=data.name, uid=data.uid)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def update_user_name_by_id(db: Session, user_id: int, name: str):
    """회원 정보 수정 쿼리"""
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.name = name
        db.commit()
        db.refresh(user)

    return user
