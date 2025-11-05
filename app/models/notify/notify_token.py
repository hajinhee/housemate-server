from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, String, Boolean, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship


class NotifyToken(Base):
    __tablename__ = "notify_tokens"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False, index=True)
    device_type = Column(String(50), nullable=False)
    is_active = Column(Boolean, default=True)
    token = Column(String(255), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 관계 연결
    user = relationship(
        "User", back_populates="notify_tokens"
    )  # NotifyToken -> User 간의 N:1 (users.id를 통한 참조)
