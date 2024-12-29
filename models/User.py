from sqlalchemy import Column, Integer, String, Boolean, DateTime
from db.database import Base
from datetime import datetime
from sqlalchemy.orm import relationship
# from models.Cart import Cart

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False)
    address = Column(String, nullable=False)
    contact = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    cart = relationship("Cart", back_populates="user")

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # carts = relationship("Cart", back_populates="user", cascade="all, delete")