import os
import shutil

from fastapi import APIRouter, File, UploadFile
from fastapi.responses import FileResponse

router = APIRouter(prefix="/file", tags=["file"])


@router.post("/")
def get_file(file: bytes = File(...)):
    content = file.decode("utf-8")
    lines = content.split("\n")
    return {"lines": lines}


@router.post("/uploadfile")
def get_uploadfile(upload_file: UploadFile = File(...)):
    full_path = os.path.join(
        os.path.abspath(os.curdir), "files", f"{upload_file.filename}"
    )
    with open(full_path, "w+b") as buffer:
        try:
            shutil.copyfileobj(upload_file.file, buffer)
        except Exception as e:
            print(e)

    return {"filename": full_path, "type": upload_file.content_type}


@router.get("/download/{name}", response_class=FileResponse)
def get_file(name: str):
    path = f"files/{name}"
    return path