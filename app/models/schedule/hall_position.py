from sqlalchemy import BigInteger, Column, String, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import relationship


class HallPosition(Base):
    __tablename__ = "hall_positions"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    hall_id = Column(BigInteger, ForeignKey("halls.id"), nullable=False)
    name = Column(String(100), nullable=False)

    # 관계 연결
    hall = relationship(
        "Hall", back_populates="hall_positions"
    )  # HallPosition -> Hall 간의 N:1 (halls.id를 통한 참조)
