import httpx
from django.conf import settings


def check_platform_health() -> dict:
    try:
        resp = httpx.get(f"{settings.BACKEND_API_URL}/health", timeout=2.0)
        backend = resp.json() if resp.status_code == 200 else {"status": "degraded"}
    except Exception:
        backend = {"status": "unreachable"}
    return {"frontend": "healthy", "backend": backend}
