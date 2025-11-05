from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    uid = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_at = Column(DateTime, nullable=True)

    # 관계
    group_users = relationship(
        "GroupUser", back_populates="user"
    )  # User -> GroupUser 간의 1:N (user.id를 통한 참조)
    notice_reads = relationship(
        "NoticeRead", back_populates="user"
    )  # User -> NoticeRead 간의 1:N (user.id를 통한 참조)
    notify_histories = relationship(
        "NotifyHistory", back_populates="user"
    )  # User -> NotifyHistory 간의 1:N (user.id를 통한 참조)
    notify_tokens = relationship(
        "NotifyToken", back_populates="user"
    )  # User -> NotifyToken 간의 1:N (users.id를 통한 참조)
    notify_topics = relationship(
        "NotifyTopic", back_populates="user"
    )  # User -> NotifyTopic 간의 1:N (users.id를 통한 참조)
    off_requests = relationship(
        "OffRequest", back_populates="user"
    )  # User -> OffRequest 간의 1:N (users.id를 통한 참조)
    schedule_requests = relationship(
        "ScheduleRequest",
        back_populates="user",
        foreign_keys="ScheduleRequest.user_id",
    )
    requested_replacements = relationship(
        "ScheduleRequest",
        back_populates="replacement_member",
        foreign_keys="ScheduleRequest.replacement_member_id",
    )
    schedules = relationship(
        "Schedule", back_populates="user"
    )  # User -> Schedule 간의 1:N (users.id를 통한 참조)
