import httpx
from django.conf import settings

FALLBACK_PILLARS = [
    {
        "slug": "data-analytics-ai-solutions",
        "code": "01 // AI",
        "title": "Data Analytics & AI Solutions",
        "tagline": "Enterprise RAG, Agentic AI, MCP Servers & BI",
        "summary": "Governed Generative AI systems and analytics platforms featuring domain-grounded RAG, MCP tool servers, and multi-agent workflows.",
        "deliverables": ["Enterprise Knowledge RAG Engines", "Stateful Agentic AI Workflows", "Custom MCP Servers & BI Dashboards"],
        "tech_stack": ["LangGraph", "MCP", "Pydantic", "pgvector", "Power BI"],
        "business_impact": "60% reduction in knowledge retrieval time",
    },
    {
        "slug": "intelligent-automation-rpa",
        "code": "02 // RPA",
        "title": "Intelligent Automation & RPA",
        "tagline": "UiPath, Power Automate, Automation Anywhere, Blue Prism & IDP",
        "summary": "Eliminate repetitive back-office operations using enterprise RPA bots and AI-powered intelligent document processing.",
        "deliverables": ["Unattended & Attended RPA Bots", "Intelligent Document Processing (IDP)", "Cross-Platform ERP & Workflow Sync"],
        "tech_stack": ["UiPath", "Power Automate", "Automation Anywhere", "Blue Prism", "IDP"],
        "business_impact": "70%+ manual processing hours reclaimed",
    },
    {
        "slug": "custom-software-app-development",
        "code": "03 // DEV",
        "title": "Custom Software & App Development",
        "tagline": "Cloud-Native Platforms, APIs & Microservices",
        "summary": "High-throughput web platforms, asynchronous backends, and resilient microservices built for enterprise scale.",
        "deliverables": ["Custom SaaS & Enterprise Web Portals", "High-Performance REST/GraphQL APIs", "Microservices Modernization"],
        "tech_stack": ["Python", "FastAPI", "Django", "PostgreSQL"],
        "business_impact": "Sub-50ms API latency with 99.95% uptime SLA",
    },
    {
        "slug": "it-strategy-digital-transformation",
        "code": "04 // ADV",
        "title": "IT Strategy & Digital Transformation",
        "tagline": "Enterprise Architecture, Roadmaps & Technical Audits",
        "summary": "Align technology investments with measurable business KPIs through enterprise blueprints and modernization roadmaps.",
        "deliverables": ["Target-State Architecture Blueprints", "Legacy Modernization & Technical Audits", "Digital Transformation Roadmaps"],
        "tech_stack": ["TOGAF", "Enterprise Architecture", "System Design", "FinOps"],
        "business_impact": "35% faster architecture sign-off",
    },
    {
        "slug": "cybersecurity-compliance",
        "code": "05 // SEC",
        "title": "Cybersecurity & Compliance",
        "tagline": "Zero-Trust Architecture, Audits & Governance",
        "summary": "Safeguard enterprise workloads and data with zero-trust security frameworks, continuous compliance audits, and risk governance.",
        "deliverables": ["Zero-Trust Security Architecture", "Security & Compliance Audits", "Identity, Access & Risk Governance"],
        "tech_stack": ["Zero-Trust", "IAM", "SOC2 / ISO 27001", "SIEM"],
        "business_impact": "80% reduction in critical security vulnerabilities",
    },
    {
        "slug": "cloud-infrastructure",
        "code": "06 // CLD",
        "title": "Cloud & Infrastructure (AWS, Azure, GCP)",
        "tagline": "Cloud Migration, Kubernetes, Terraform & Server Management",
        "summary": "Seamless multi-cloud migrations, automated Infrastructure-as-Code, container orchestration, and resilient server operations.",
        "deliverables": ["Multi-Cloud Migration & Modernization", "Kubernetes & Terraform IaC", "Automated Server & Network Management"],
        "tech_stack": ["AWS", "Azure", "GCP", "Kubernetes", "Terraform"],
        "business_impact": "40% faster infrastructure provisioning & cloud cost optimization",
    },
    {
        "slug": "managed-it-services-support",
        "code": "07 // OPS",
        "title": "Managed IT Services / Support",
        "tagline": "AIOps Observability, Cloud SRE & 24/7 L2/L3 SLA Support",
        "summary": "Proactive AIOps anomaly detection, site reliability engineering, incident management, and round-the-clock production support.",
        "deliverables": ["AIOps Observability & Self-Healing Runbooks", "Cloud SRE & Incident Management", "24/7 L2/L3 SLA Production Support"],
        "tech_stack": ["Prometheus", "Grafana", "AIOps", "ITSM / Helpdesk"],
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
