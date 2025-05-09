from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes.user import router as user_router
from app.routes.blog import router as blog_router

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routes
app.include_router(user_router)
app.include_router(blog_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Blog"}
