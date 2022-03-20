from fastapi import FastAPI
from db import user_model
from db.database import engine

from routers import user_router, blog_router, article_router

app = FastAPI()
app.include_router(user_router.router)
app.include_router(article_router.router)
app.include_router(blog_router.router)


@app.get("/")
def index():
    return {"message": "Hello World!"}


user_model.Base.metadata.create_all(engine)
