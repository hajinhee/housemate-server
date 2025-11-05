from sqlalchemy import BigInteger, Column, String, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship


class Hall(Base):
    __tablename__ = "halls"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    group_id = Column(BigInteger, ForeignKey("groups.id"), nullable=False)

    # 관계 연결
    hall_positions = relationship(
        "HallPosition", back_populates="hall"
    )  # Hall -> HallPosition 간의 1:N (halls.id를 통한 참조)
    group = relationship(
        "Group", back_populates="halls"
    )  # Hall -> Group 간의 N:1 (groups.id를 통한 참조)
    performances = relationship(
        "Performance", back_populates="hall"
    )  # Hall -> Performance 간의 1:N (hall.id를 통한 참조)
