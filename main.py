from fastapi import FastAPI
from routers import blog_router
from db import user_model
from db.database import engine

app = FastAPI()
app.include_router(blog_router.router)


@app.get("/")
def index():
    return {"message": "Hello World!"}


user_model.Base.metadata.create_all(engine)
