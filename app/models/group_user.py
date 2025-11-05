from sqlalchemy import BigInteger, Column, Enum, ForeignKey, String
from sqlalchemy.orm import relationship
from app.db.base import Base


class GroupUser(Base):
    __tablename__ = "group_users"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    user_id = Column(BigInteger, ForeignKey("users.id"), nullable=False, index=True)
    group_id = Column(BigInteger, ForeignKey("groups.id"), nullable=False, index=True)
    role = Column(Enum("LEADER", "MEMBER", name="group_user_roles"), nullable=False)
    status = Column(
        Enum("REQUEST", "ACCEPTED", "REJECTED", name="group_user_status"),
        nullable=False,
    )

    # 관계
    user = relationship(
        "User", back_populates="group_users"
    )  # GroupUser -> User 간의 N:1 (users.id를 통한 참조)
    group = relationship(
        "Group", back_populates="group_users"
    )  # GroupUser -> Group 간의 N:1 (groups.id를 통한 참조)
