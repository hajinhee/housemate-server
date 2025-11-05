from datetime import datetime
from sqlalchemy import BigInteger, Column, Date, DateTime, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship


class OffRequest(Base):
    __tablename__ = "off_requests"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    group_id = Column(BigInteger, ForeignKey("groups.id"), nullable=False, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False, index=True)
    date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 관계 연결
    group = relationship(
        "Group", back_populates="off_requests"
    )  # OffRequest -> Group 간의 N:1 (groups.id를 통한 참조)
    user = relationship(
        "User", back_populates="off_requests"
    )  # OffRequest -> User 간의 N:1 (users.id를 통한 참조)
