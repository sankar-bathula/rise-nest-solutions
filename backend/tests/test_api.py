import pytest
from httpx import ASGITransport, AsyncClient
from app.main import app


@pytest.mark.asyncio
async def test_five_practice_pillars_seeded():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        res = await client.get("/api/v1/services")
        assert res.status_code == 200
        slugs = [s["slug"] for s in res.json()]
        assert slugs == [
            "consultancy",
            "application-development",
            "ai-services",
            "automation",
            "it-operations",
        ]


@pytest.mark.asyncio
async def test_create_inquiry_and_admin_guard():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as client:
        payload = {
            "full_name": "Rakesh Sharma",
            "work_email": "rakesh@globalfin.io",
            "company_name": "GlobalFin Corp",
            "phone": "+91-9000011111",
            "service_slug": "automation",
            "project_scope": "Need enterprise UiPath invoice automation integrated with SAP.",
        }
        create_res = await client.post("/api/v1/inquiries", json=payload)
        assert create_res.status_code == 201
        data = create_res.json()
        assert data["reference_id"].startswith("RNS-")
        assert data["priority_tag"] == "ENTERPRISE-FASTTRACK"

        unauth = await client.get("/api/v1/inquiries")
        assert unauth.status_code in (401, 422)
