from typing import Optional, List
from fastapi import APIRouter, Response, Header

router = APIRouter(prefix="/product", tags=["product"])

products = ["watch", "camera", "phone"]


@router.get("/")
def get_all_product():
    data = " ".join(products)
    return Response(content=data, media_type="text/plain")


@router.get("/withheader")
def get_product(response: Response, custom_header: Optional[str] = Header(None)):
    return products

@router.get("/with_list_header")
def get_product(response: Response, custom_header: Optional[List[str]] = Header(None)):
    response.headers["custom_response_header"] = ", ".join(custom_header)
    return products
