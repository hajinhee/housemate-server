from datetime import datetime
from sqlalchemy import BigInteger, Column, DateTime, String, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship


class NotifyTopic(Base):
    __tablename__ = "notify_topics"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    group_id = Column(BigInteger, ForeignKey("groups.id"), nullable=False, index=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False, index=True)
    group_name = Column(String(255), nullable=False)
    user_token = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 관계 연결
    group = relationship(
        "Group", back_populates="notify_topics"
    )  # NotifyTopic -> Group 간의 N:1 (groups.id를 통한 참조)
    user = relationship(
        "User", back_populates="notify_topics"
    )  # NotifyTopic -> User 간의 N:1 (users.id를 통한 참조)
