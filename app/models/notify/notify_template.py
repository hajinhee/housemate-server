from sqlalchemy import BigInteger, Column, String
from app.db.base import Base
from sqlalchemy.orm import relationship


class NotifyTemplate(Base):
    __tablename__ = "notify_templates"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    key = Column(String(100), nullable=False)
    title = Column(String(255), nullable=False)
    content = Column(String(1000), nullable=False)
    deeplink = Column(String(255), nullable=True)
