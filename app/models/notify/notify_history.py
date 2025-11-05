from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, String, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship


class NotifyHistory(Base):
    __tablename__ = "notify_histories"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    notice_id = Column(BigInteger, ForeignKey("notices.id"), nullable=False)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String(1000))
    deeplink = Column(String(255))
    read_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 관계 연결
    notice = relationship(
        "Notice", back_populates="notify_histories"
    )  # NotifyHistory -> Notice 간의 N:1 (notices.id를 통한 참조)
    user = relationship(
        "User", back_populates="notify_histories"
    )  # NotifyHistory -> User 간의 N:1 (users.id를 통한 참조)
