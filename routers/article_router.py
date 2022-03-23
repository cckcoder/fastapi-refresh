from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends
from typing import List

from schemas import ArticleBase, ArticleDisplay, UserBase
from db.database import get_db
from db import db_article
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix="/article", tags=["article"], dependencies=[Depends(get_current_user)]
)

# Create article
@router.post("/", response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db)):
    return db_article.create_article(db, request)


@router.get("/", response_model=List[ArticleDisplay])
def get_all_article(db: Session = Depends(get_db)):
    # Handle error
    return db_article.get_all_article(db)


# Get articles
@router.get("/{article_id}", response_model=ArticleDisplay)
def get_article(
    article_id: int,
    db: Session = Depends(get_db),
):
    return db_article.get_article(db, article_id)
