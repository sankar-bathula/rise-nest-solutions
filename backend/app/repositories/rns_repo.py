from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.domain import ClientInquiry, ServicePillar


class ServiceRepository:
    @staticmethod
    async def get_all(db: AsyncSession) -> list[ServicePillar]:
        result = await db.execute(select(ServicePillar).order_by(ServicePillar.display_order))
        return list(result.scalars().all())

    @staticmethod
    async def get_by_slug(db: AsyncSession, slug: str) -> ServicePillar | None:
        result = await db.execute(select(ServicePillar).where(ServicePillar.slug == slug))
        return result.scalar_one_or_none()


class InquiryRepository:
    @staticmethod
    async def create(db: AsyncSession, inquiry: ClientInquiry) -> ClientInquiry:
        db.add(inquiry)
        await db.commit()
        await db.refresh(inquiry)
        return inquiry

    @staticmethod
    async def list_all(db: AsyncSession) -> list[ClientInquiry]:
        result = await db.execute(select(ClientInquiry).order_by(ClientInquiry.created_at.desc()))
        return list(result.scalars().all())
