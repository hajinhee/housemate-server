from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class Group(Base):
    __tablename__ = "groups"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    code = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 관계
    group_users = relationship(
        "GroupUser", back_populates="group"
    )  # Group -> GroupUser 간의 1:N (groups.id를 통한 참조)
    notices = relationship(
        "Notice", back_populates="group"
    )  # Group -> Notice 간의 1:N (groups.id를 통한 참조)
    notify_topics = relationship(
        "NotifyTopic", back_populates="group"
    )  # Group -> NotifyTopic 간의 1:N (groups.id를 통한 참조)
    halls = relationship(
        "Hall", back_populates="group"
    )  # Group -> Hall 간의 1:N (groups.id를 통한 참조)
    off_requests = relationship(
        "OffRequest", back_populates="group"
    )  # Group -> OffRequest 간의 1:N (groups.id를 통한 참조)
    performances = relationship(
        "Performance", back_populates="group"
    )  # Group -> Performance 간의 1:N (groups.id를 통한 참조)
    schedules = relationship(
        "Schedule", back_populates="group"
    )  # Group -> Schedule 간의 1:N (groups.id를 통한 참조)
