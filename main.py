from fastapi import FastAPI
from API.profile import router as user_router
from API.CartAPI import router as cart_router
from db.database import Base, engine

app = FastAPI()

@app.get('/')
async def root():
    return {
        'message': 'Welcome to the FastAPI framework!'
    }


Base.metadata.create_all(bind=engine)


app.include_router(user_router, prefix="/users", tags=["users"])  # User-related endpoints
app.include_router(cart_router, prefix="/carts", tags=["carts"])  # Cart-related endpoints
