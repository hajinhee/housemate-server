from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, Date, Time, String, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship


class Performance(Base):
    __tablename__ = "performances"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    group_id = Column(BigInteger, ForeignKey("groups.id"), nullable=False, index=True)
    hall_id = Column(BigInteger, ForeignKey("halls.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False)
    date = Column(Date, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 관계 연결
    group = relationship(
        "Group", back_populates="performances"
    )  # Performance -> Group 간의 N:1 (groups.id를 통한 참조)
    hall = relationship(
        "Hall", back_populates="performances"
    )  # Performance -> Hall 간의 N:1 (halls.id를 통한 참조)
