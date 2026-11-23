from fastapi import APIRouter

router = APIRouter()


@router.get("")
async def health_check():
    return {"status": "healthy", "service": "RNS Backend API", "version": "1.0.0"}
