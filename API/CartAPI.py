from Schemas.CartSchema import CartCreate, CartOut
from db.database import get_db, Session
from fastapi import APIRouter, Depends, HTTPException
from models.Cart import Cart

router = APIRouter()

@router.get("/carts", response_model=list[CartOut])
def get_all_carts(db: Session = Depends(get_db)):
    carts = db.query(Cart).all()
    if not carts:
        raise HTTPException(status_code=404, detail="No carts found")
    return carts

@router.post("/carts", response_model=CartOut)
def create_cart(cart_data: CartCreate, db: Session = Depends(get_db)):
    new_cart = Cart(
        user_id=cart_data.user_id,
        items=cart_data.items,
        total_price=cart_data.total_price
    )
    db.add(new_cart)
    db.commit()
    db.refresh(new_cart)
    return new_cart
