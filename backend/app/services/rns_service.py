import uuid
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.domain import ClientInquiry
from app.repositories.rns_repo import InquiryRepository, ServiceRepository
from app.schemas.rns_schemas import InquiryCreate


class RNSService:
    @staticmethod
    async def fetch_catalog(db: AsyncSession):
        return await ServiceRepository.get_all(db)

    @staticmethod
    async def fetch_service_detail(db: AsyncSession, slug: str):
        return await ServiceRepository.get_by_slug(db, slug)

    @staticmethod
    async def register_inquiry(db: AsyncSession, payload: InquiryCreate) -> ClientInquiry:
        date_stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
        short_hash = uuid.uuid4().hex[:5].upper()
        ref_id = f"RNS-{date_stamp}-{short_hash}"

        scope_lower = payload.project_scope.lower()
        priority = (
            "ENTERPRISE-FASTTRACK"
            if any(k in scope_lower for k in ("urgent", "enterprise", "migration", "production", "24/7"))
            else "STANDARD"
        )

        inquiry = ClientInquiry(
            reference_id=ref_id,
            full_name=payload.full_name.strip(),
            work_email=payload.work_email.lower().strip(),
            company_name=payload.company_name.strip(),
            phone=payload.phone.strip() if payload.phone else None,
            service_slug=payload.service_slug,
            project_scope=payload.project_scope.strip(),
            priority_tag=priority,
        )
        return await InquiryRepository.create(db, inquiry)

    @staticmethod
    async def list_inquiries(db: AsyncSession):
        return await InquiryRepository.list_all(db)
