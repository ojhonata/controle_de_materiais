from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from data.conf.db_session import get_session
from schemas.user_schema import UserCreate, UserResponse
from service import user_service

router = APIRouter()


@router.get("/users", response_model=list[UserResponse])
async def list_users(session: Session = Depends(get_session)):
    return user_service.get_all(session)


@router.get("/user", response_model=UserResponse)
async def list_by_cs(cs: int, session: Session = Depends(get_session)):
    try:
        return user_service.get_user_by_cs(session, cs)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.post("/user_create", response_model=UserCreate)
async def create_user(data: UserCreate, session: Session = Depends(get_session)):
    try:
        return user_service.post_user(session, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
