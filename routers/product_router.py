from time import time
from typing import Optional, List
import time

from fastapi import APIRouter, Cookie, Form, Response, Header

router = APIRouter(prefix="/product", tags=["product"])

products = ["watch", "camera", "phone"]

async def time_consuming_functionality():
    time.sleep(5)
    return "ok"



@router.get("/")
async def get_all_product():
    await time_consuming_functionality()
    data = " ".join(products)
    response = Response(content=data, media_type="text/plain")
    response.set_cookie(key="test_cookie", value="test_cookie_value")
    return response


@router.get("/withheader")
def get_product(
    response: Response,
    custom_header: Optional[str] = Header(None),
    test_cookie: Optional[str] = Cookie(None),
):
    return {"data": products, "cookie": test_cookie}


@router.get("/with_list_header")
def get_product(response: Response, custom_header: Optional[List[str]] = Header(None)):
    response.headers["custom_response_header"] = ", ".join(custom_header)
    return products


@router.post("/new")
def create_product(name: str = Form(...)):
    products.append(name)
    return products
