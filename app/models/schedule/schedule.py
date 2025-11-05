from datetime import datetime
from sqlalchemy import BigInteger, Column, Date, DateTime, Time, String, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship


class Schedule(Base):
    __tablename__ = "schedules"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    group_id = Column(BigInteger, ForeignKey("groups.id"), nullable=False, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False, index=True)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    position = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 관계 연결
    group = relationship(
        "Group", back_populates="schedules"
    )  # Schedule -> Group 간의 N:1 (groups.id를 통한 참조)
    user = relationship(
        "User", back_populates="schedules"
    )  # Schedule -> User 간의 N:1 (users.id를 통한 참조)
    schedule_requests = relationship(
        "ScheduleRequest", back_populates="schedule"
    )  # Schedule -> ScheduleRequest 간의 1:N (schedules.id를 통한 참조)
