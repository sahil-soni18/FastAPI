from Schemas.UserSchema import UserOut, UserBase, UserCreate
from db.database import get_db, Session
from fastapi import APIRouter, Depends, HTTPException
from models.User import User
from passlib.context import CryptContext

router = APIRouter()


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@router.get("/users", response_model=list[UserOut])
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users


@router.post('/register', response_model=UserOut)
async def register( user_data: UserCreate, db: Session = Depends(get_db)):
    newUser = User(
        name=user_data.name,
        email=user_data.email,
        address=user_data.address,
        contact=user_data.contact,
        is_admin=user_data.is_admin,
        password_hash=hash_password(user_data.password)
    )

    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser
