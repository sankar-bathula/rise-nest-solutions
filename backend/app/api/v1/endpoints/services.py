from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.schemas.rns_schemas import ServicePillarOut
from app.services.rns_service import RNSService

router = APIRouter()


@router.get("", response_model=list[ServicePillarOut])
async def get_all_services(db: AsyncSession = Depends(get_db)):
    return await RNSService.fetch_catalog(db)


@router.get("/{slug}", response_model=ServicePillarOut)
async def get_service_by_slug(slug: str, db: AsyncSession = Depends(get_db)):
    service = await RNSService.fetch_service_detail(db, slug)
    if not service:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Service pillar not found")
    return service
