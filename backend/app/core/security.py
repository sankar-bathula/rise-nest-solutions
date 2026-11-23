from fastapi import Header, HTTPException, status
from app.core.config import settings


async def verify_admin_key(x_api_key: str = Header(..., description="Admin API Key")):
    if x_api_key != settings.ADMIN_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing X-API-Key header.",
        )
    return True
