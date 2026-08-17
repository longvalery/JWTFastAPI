from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..models.database import get_db
from ..schemas.user import UserResponse, UserOut
from ..core.dependencies import get_current_user
from ..models.users import User

router = APIRouter(prefix="/api/users", tags=["users"])

# @router.get("/me", response_model=UserResponse)
# def get_current_user_info(current_user: User = Depends(get_current_user)):
#     """
#     Получение информации о текущем пользователе.
#     Эндпоинт защищён: требуется валидный access токен.
#     """
#     return current_user

@router.get("/me", response_model=UserOut)
async def read_current_user(token: str,
                      db: Session = Depends(get_db)):
        # current_user: User = Depends(get_current_user)):
    current_user = await get_current_user(token, db)
    """Получить информацию о текущем пользователе"""
    return current_user