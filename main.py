from enum import Enum
from typing import Optional
from fastapi import FastAPI, Response, status


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World!"}


@app.get(
    "/blog/all",
    tags=["blog"],
    summary="Retrieve all blogs",
    description="This api call simulates refresh blog",
)
def get_all_blog(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@app.get("/blog/{id}/comments/{comment_id}", tags=["blog", "comment"])
def get_comment(
    id: int, comment_id: int, valid: bool = True, username: Optional[str] = None
):
    """
    Simulates retrieving a comment of a blog
    - **id** mandatory path parameter
    - **comment_id** optional query parameter
    - **valid** optional query parameter
    - **username** optional query parameter
    """
    return {
        "message": f"blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}"
    }


class BlogType(str, Enum):
    short = "short"
    story = "story"
    howto = "howto"


@app.get("/blog/type/{type}", tags=["blog"])
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


@app.get("/blog/{id}", status_code=status.HTTP_200_OK, tags=["blog"])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"blog {id} not found"}
    return {"message": f"Blog with id {id}"}
