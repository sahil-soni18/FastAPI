from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CartBase(BaseModel):
    items: Optional[dict] = {}  # JSON structure for cart items
    total_price: int = 0  # Total price of cart items

class CartCreate(CartBase):
    user_id: int  # User ID to associate with the cart

class CartOut(CartBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
