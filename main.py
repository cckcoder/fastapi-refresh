from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from db import user_model
from db.database import engine

from routers import user_router, blog_router, article_router, product_router
from utils.exceptions import StoryException

app = FastAPI()
app.include_router(user_router.router)
app.include_router(article_router.router)
app.include_router(blog_router.router)
app.include_router(product_router.router)


@app.get("/")
def index():
    return {"message": "Hello World!"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=status.HTTP_418_IM_A_TEAPOT, content={"detail": exc.name}
    )


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)


user_model.Base.metadata.create_all(engine)
