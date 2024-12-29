from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
from .CartSchema import CartOut

class UserBase(BaseModel):
    name: str
    email: EmailStr
    address: str
    contact: str
    is_admin: bool = False  

class UserCreate(UserBase):
    password: str  # Password field for creating a user

class UserUpdate(UserBase):
    password: Optional[str] = None  # Password field is optional for updating a user
    is_admin: Optional[bool] = None  # Admin field is optional for updating a user
    address: Optional[str] = None  # Address field is optional for updating a user
    contact: Optional[str] = None  # Contact field is optional for updating a user
    name: Optional[str] = None  # Name field is optional for updating a user
    email: Optional[EmailStr] = None  # Email field is optional for updating a user
    

class UserOut(UserBase):
    id: int
    cart: Optional[List['CartOut']] = []  # Optional relationship to cart

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True  # Pydantic will treat the SQLAlchemy models as dictionaries.

