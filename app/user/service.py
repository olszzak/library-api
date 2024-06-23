from fastapi import Depends
from sqlalchemy.orm import Session

from app.misc.db_base_service import BaseService
from app.misc.deps import get_db
from app.user.schema import CreateUserSchema
from app.user.model import User


class UserService(BaseService[User, CreateUserSchema]):
    def __init__(self, db_session: Session):
        super(UserService, self).__init__(User, db_session)


def get_users_service(db_session: Session = Depends(get_db)) -> UserService:
    return UserService(db_session)
