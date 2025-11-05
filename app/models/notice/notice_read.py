from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class NoticeRead(Base):
    __tablename__ = "notice_reads"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    notice_id = Column(BigInteger, ForeignKey("notices.id"), nullable=False, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False, index=True)
    read_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    notice = relationship(
        "Notice", back_populates="reads"
    )  # NoticeRead -> Notice 간의 N:1 (notices.id를 통한 참조)
    user = relationship(
        "User", back_populates="notice_reads"
    )  # NoticeRead -> User 간의 N:1 (users.id를 통한 참조)
