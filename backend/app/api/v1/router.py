from fastapi import APIRouter
from app.api.v1.endpoints import health, inquiries, services

api_router = APIRouter()
api_router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(services.router, prefix="/services", tags=["Services"])
api_router.include_router(inquiries.router, prefix="/inquiries", tags=["Inquiries"])
