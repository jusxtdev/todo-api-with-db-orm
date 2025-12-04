from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.users import UserCreate, UserResponse, UserUpdate
from app.utils import raise_error_404

router = APIRouter(prefix='/users', tags=['Users'])

@router.post('/', response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(new_user_data : UserCreate, db : Session = Depends(get_db)):
    new_user = User(username = new_user_data.username)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user