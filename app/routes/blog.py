from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.db.database import SessionLocal
from app.models.blog import Blog
from app.schemas.blog import BlogCreate, BlogOut

router = APIRouter(prefix="/blogs", tags=["blogs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BlogOut, status_code=status.HTTP_201_CREATED)
def create_blog(blog_in: BlogCreate, db: Session = Depends(get_db)):
    new_blog = Blog(title=blog_in.title, content=blog_in.content, owner_id=1)  # TODO: real user
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/", response_model=List[BlogOut])
def list_blogs(db: Session = Depends(get_db)):
    return db.query(Blog).all()

@router.get("/{blog_id}", response_model=BlogOut)
def get_blog(blog_id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")
    return blog
