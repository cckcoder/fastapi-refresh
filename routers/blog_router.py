from enum import Enum
from typing import List, Optional
from fastapi import APIRouter, Response, status, Body, Query
from pydantic import BaseModel

router = APIRouter(prefix="/blog", tags=["blog"])


@router.get(
    "/all",
    summary="Retrieve all blogs",
    description="This api call simulates refresh blog",
    response_description="The list of available blogs",
)
def get_all_blog(page=1, page_size: Optional[int] = None):
    return {"message": f"All {page_size} blogs on page {page}"}


@router.get("/{id}/comments/{comment_id}", tags=["comment"])
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


@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"Blog type {type}"}


@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"blog {id} not found"}
    return {"message": f"Blog with id {id}"}


class BlogModel(BaseModel):
    title: str
    content: str
    nb_comments: int
    published: Optional[bool]


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    print(blog.title)
    return {
         "id": id,
         "data": blog ,
         "version": version
        }

@router.post("/new/{id}/comment")
def create_comment(
    blog: BlogModel,
    id: int,
    commend_id: int = Query(
        None,
        title="Id of the comment",
        description="Some description for comment_id",
        alias="commentId",
        deprecated=True
    ),
    content: str = Body(...,
        min_length=10,
        max_length=12,
        regex="^[a-z\s]*$"
    ),
    v: Optional[List[str]] = Query(None)
 ):
    return {
        "blog": blog,
        "id": id,
        "comment_id": commend_id,
        "content": content,
        "version": v
    }