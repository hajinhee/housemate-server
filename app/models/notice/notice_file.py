from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class NoticeFile(Base):
    __tablename__ = "notice_files"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    notice_id = Column(BigInteger, ForeignKey("notices.id"), nullable=False)
    s3_bucket = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    notice = relationship(
        "Notice", back_populates="files"
    )  # NoticeFile -> Notice 간의 N:1 (notices.id를 통한 참조)
