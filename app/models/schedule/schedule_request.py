from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, Time, String, Enum, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship


class ScheduleRequest(Base):
    __tablename__ = "schedule_requests"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    schedule_id = Column(
        BigInteger, ForeignKey("schedules.id"), nullable=False, index=True
    )
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False, index=True)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    replacement_member_id = Column(BigInteger, ForeignKey("users.id"), nullable=True)
    reason = Column(String(255), nullable=True)
    request_type = Column(
        Enum("OFF", "ABSENCE", "REPLACEMENT", name="schedule_request_type_enum"),
        nullable=False,
    )
    status = Column(
        Enum("REQUEST", "ACCEPTED", "REJECTED", name="schedule_request_status_enum"),
        default="REQUEST",
    )

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 관계 연결
    schedule = relationship(
        "Schedule", back_populates="schedule_requests"
    )  # ScheduleRequest -> Schedule 간의 N:1 (schedules.id를 통한 참조)
    user = relationship(
        "User",
        foreign_keys=[user_id],
        back_populates="schedule_requests",
    )  # ScheduleRequest -> User 간의 N:1 (users.id를 통한 참조)
    replacement_member = relationship(
        "User",
        foreign_keys=[replacement_member_id],
        back_populates="requested_replacements",
    )  # ScheduleRequest -> User 간의 N:1 (replacement_member_id를 통한 참조)
