from fastapi import FastAPI
from db import user_model
from db.database import engine

from routers import blog_router
from routers import user_router

app = FastAPI()
app.include_router(user_router.router)
app.include_router(blog_router.router)


@app.get("/")
def index():
    return {"message": "Hello World!"}


user_model.Base.metadata.create_all(engine)
