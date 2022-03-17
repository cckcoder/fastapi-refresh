import pdb
from click import password_option
from sqlalchemy.orm.session import Session
from db.hash import Hash
from schemas import UserBase
from db.user_model import DbUser


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username=request.username,
        email=request.email,
        password = Hash.bcrypt(request.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
