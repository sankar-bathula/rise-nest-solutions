from datetime import datetime
from typing import Literal
from pydantic import BaseModel, ConfigDict, EmailStr, Field

ServiceSlug = Literal[
    "consultancy",
    "application-development",
    "ai-services",
    "automation",
    "it-operations",
]


class ServicePillarOut(BaseModel):
    id: int
    slug: str
    code: str
    title: str
    tagline: str
    summary: str
    deliverables: list[str]
    tech_stack: list[str]
    business_impact: str
    display_order: int

    model_config = ConfigDict(from_attributes=True)


class InquiryCreate(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=120)
    work_email: EmailStr
    company_name: str = Field(..., min_length=2, max_length=160)
    phone: str | None = Field(default=None, max_length=32)
    service_slug: ServiceSlug
    project_scope: str = Field(..., min_length=10, max_length=3000)


class InquiryOut(BaseModel):
    id: int
    reference_id: str
    full_name: str
    work_email: EmailStr
    company_name: str
    phone: str | None
    service_slug: str
    project_scope: str
    priority_tag: str
    is_resolved: bool
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
