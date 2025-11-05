from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class Notice(Base):
    __tablename__ = "notices"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    group_id = Column(BigInteger, ForeignKey("groups.id"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    is_fix = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 관계 연결
    images = relationship(
        "NoticeImage", back_populates="notice"
    )  # Notice -> NoticeImage 간의 1:N (notices.id를 통한 참조)
    files = relationship(
        "NoticeFile", back_populates="notice"
    )  # Notice -> NoticeFile 간의 1:N (notices.id를 통한 참조)
    reads = relationship(
        "NoticeRead", back_populates="notice"
    )  # Notice -> NoticeRead 간의 1:N (notice.id를 통한 참조)
    group = relationship(
        "Group", back_populates="notices"
    )  # Notice -> Group 간의 N:1 (groups.id를 통한 참조)
    notify_histories = relationship(
        "NotifyHistory", back_populates="notice"
    )  # Notice -> NotifyHistory 간의 1:N (notices.id를 통한 참조)
