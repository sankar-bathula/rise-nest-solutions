from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import verify_admin_key
from app.db.session import get_db
from app.schemas.rns_schemas import InquiryCreate, InquiryOut
from app.services.rns_service import RNSService

router = APIRouter()


@router.post("", response_model=InquiryOut, status_code=status.HTTP_201_CREATED)
async def submit_inquiry(payload: InquiryCreate, db: AsyncSession = Depends(get_db)):
    return await RNSService.register_inquiry(db, payload)


@router.get("", response_model=list[InquiryOut], dependencies=[Depends(verify_admin_key)])
async def get_inquiries(db: AsyncSession = Depends(get_db)):
    return await RNSService.list_inquiries(db)
