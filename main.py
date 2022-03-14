from fastapi import FastAPI
from routers import blog_router


app = FastAPI()
app.include_router(blog_router.router)


@app.get("/")
def index():
    return {"message": "Hello World!"}