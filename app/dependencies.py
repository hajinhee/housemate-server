# app/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.db.session import get_db
from sqlalchemy.orm import Session

from app.models.user import User
from app.utils.jwt_handeler import verify_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    payload = verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
        )

    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=401, detail="Missing user info")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user
