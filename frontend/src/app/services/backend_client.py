import httpx
from django.conf import settings

FALLBACK_PILLARS = [
    {
        "slug": "consultancy",
        "code": "01 // ADV",
        "title": "Consultancy",
        "tagline": "Enterprise Architecture, Digital Strategy & Technical Audits",
        "summary": "Align technology investments with measurable business KPIs through enterprise blueprints and modernization roadmaps.",
        "deliverables": ["Target-State Architecture Blueprints", "Legacy Modernization & ROI Audits", "CoE Governance Setup"],
        "tech_stack": ["TOGAF", "AWS / Azure", "System Design", "FinOps"],
        "business_impact": "35% faster architecture sign-off",
    },
    {
        "slug": "application-development",
        "code": "02 // DEV",
        "title": "Application Development",
        "tagline": "Cloud-Native Full-Stack Platforms, APIs & Microservices",
        "summary": "High-throughput web platforms, asynchronous Python backends, and resilient microservices built for scale.",
        "deliverables": ["Custom SaaS & Enterprise Web Portals", "High-Performance REST/GraphQL APIs", "Microservices Modernization"],
        "tech_stack": ["Python", "FastAPI", "Django", "PostgreSQL"],
        "business_impact": "Sub-50ms API latency with 99.95% uptime SLA",
    },
    {
        "slug": "ai-services",
        "code": "03 // AI",
        "title": "AI Services",
        "tagline": "Production LLMs, Enterprise RAG, MCP Servers & Agentic AI",
        "summary": "Governed Generative AI systems featuring domain-grounded RAG, MCP tool servers, and multi-agent workflows.",
        "deliverables": ["Enterprise Knowledge RAG Engines", "Stateful LangGraph Agents", "Custom MCP Server Integrations"],
        "tech_stack": ["LangGraph", "MCP", "Pydantic", "pgvector"],
        "business_impact": "60% reduction in knowledge retrieval time",
    },
    {
        "slug": "automation",
        "code": "04 // RPA",
        "title": "Automation",
        "tagline": "UiPath RPA Bots, Intelligent Document Processing & Workflow Sync",
        "summary": "Eliminate repetitive back-office operations using UiPath attended/unattended bots and AI document extraction.",
        "deliverables": ["UiPath Unattended/Attended Bots", "Intelligent Document Processing (IDP)", "SAP/Oracle/ERP Sync"],
        "tech_stack": ["UiPath Studio", "Orchestrator", "Python", "OCR/IDP"],
        "business_impact": "70%+ manual processing hours reclaimed",
    },
    {
        "slug": "it-operations",
        "code": "05 // OPS",
        "title": "IT Operations",
        "tagline": "AIOps Observability, Cloud SRE & 24/7 Managed Infrastructure",
        "summary": "Proactive AIOps anomaly detection, Infrastructure-as-Code, zero-downtime CI/CD, and 24/7 SRE support.",
        "deliverables": ["AIOps Self-Healing Runbooks", "Kubernetes & Terraform IaC", "24/7 L2/L3 SLA Production Support"],
        "tech_stack": ["Docker", "Kubernetes", "Terraform", "Prometheus"],
        "business_impact": "55% lower Mean Time to Resolution (MTTR)",
    },
    {
        "slug": "IT-Infrastructure-Managed-Services",
        "code": "06 // Admin",
        "title": "IT Infrastructure & Managed Services",
        "tagline": "infrastructure monitoring, server maintenance, IT support and incident management",
        "summary": "Proactive Server anomaly detection, Infrastructure-as-Code, zero-downtime CI/CD, and 24/7 SRE support.",
        "deliverables": ["Services Self-Healing Runbooks", "Kubernetes & Terraform IaC", "24/7 L2/L3 SLA Production Support"],
        "tech_stack": ["Admin", "Network", "Helpdesk", "Server Maintenance"],
        "business_impact": "68% lower Mean Time to Resolution (MTTR)",
    },
]


class BackendClient:
    @staticmethod
    def get_services() -> list[dict]:
        try:
            resp = httpx.get(f"{settings.BACKEND_API_URL}/services", timeout=3.0)
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        return FALLBACK_PILLARS

    @staticmethod
    def get_service_by_slug(slug: str) -> dict | None:
        try:
            resp = httpx.get(f"{settings.BACKEND_API_URL}/services/{slug}", timeout=3.0)
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        return next((item for item in FALLBACK_PILLARS if item["slug"] == slug), None)

    @staticmethod
    def create_inquiry(payload: dict) -> tuple[bool, dict]:
        try:
            resp = httpx.post(f"{settings.BACKEND_API_URL}/inquiries", json=payload, timeout=5.0)
            data = resp.json()
            if resp.status_code == 201:
                return True, data
            return False, {"detail": data.get("detail", "Validation error. Please verify your inputs.")}
        except Exception as exc:
            return False, {"detail": f"Backend service unreachable: {exc}"}
