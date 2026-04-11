from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from data.conf.db_session import get_session
from schemas.sector_schema import SectorCreate, SectorResponse
from service import sector_service

router = APIRouter()


@router.get("/sectors", response_model=list[SectorResponse])
async def list_sectors(session: Session = Depends(get_session)):
    return sector_service.get_all(session)


@router.get("/sector", response_model=SectorResponse)
async def list_by_name(name: str, session: Session = Depends(get_session)):
    try:
        return sector_service.get_sector_by_id(session, name)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/create", response_model=SectorCreate)
async def create_sector(data: SectorCreate, session: Session = Depends(get_session)):
    try:
        return sector_service.post_sector(session, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
