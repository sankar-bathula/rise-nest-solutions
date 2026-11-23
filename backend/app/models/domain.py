from datetime import datetime, timezone
from sqlalchemy import Boolean, DateTime, Integer, JSON, String, Text
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base


class ServicePillar(Base):
    __tablename__ = "service_pillars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    slug: Mapped[str] = mapped_column(String(64), unique=True, index=True, nullable=False)
    code: Mapped[str] = mapped_column(String(16), nullable=False)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    tagline: Mapped[str] = mapped_column(String(255), nullable=False)
    summary: Mapped[str] = mapped_column(Text, nullable=False)
    deliverables: Mapped[list[str]] = mapped_column(JSON, default=list)
    tech_stack: Mapped[list[str]] = mapped_column(JSON, default=list)
    business_impact: Mapped[str] = mapped_column(String(255), nullable=False)
    display_order: Mapped[int] = mapped_column(Integer, default=1)


class ClientInquiry(Base):
    __tablename__ = "client_inquiries"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    reference_id: Mapped[str] = mapped_column(String(24), unique=True, index=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(120), nullable=False)
    work_email: Mapped[str] = mapped_column(String(160), index=True, nullable=False)
    company_name: Mapped[str] = mapped_column(String(160), nullable=False)
    phone: Mapped[str | None] = mapped_column(String(32), nullable=True)
    service_slug: Mapped[str] = mapped_column(String(64), index=True, nullable=False)
    project_scope: Mapped[str] = mapped_column(Text, nullable=False)
    priority_tag: Mapped[str] = mapped_column(String(32), default="STANDARD")
    is_resolved: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
