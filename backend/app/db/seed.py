from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.domain import ServicePillar

RNS_PILLARS = [
    {
        "slug": "consultancy",
        "code": "01 // ADV",
        "title": "Consultancy",
        "tagline": "Enterprise Architecture, Digital Strategy & Technical Audits",
        "summary": (
            "Align technology investments with measurable business KPIs through enterprise architecture "
            "blueprints, legacy modernization roadmaps, and principal engineering advisory."
        ),
        "deliverables": [
            "Target-State Enterprise & Cloud Architecture Blueprints",
            "Legacy Modernization & TCO / ROI Assessment",
            "Data Governance, Security & Compliance Audits",
            "Fractional Principal Architect & CoE Setup",
        ],
        "tech_stack": ["TOGAF", "AWS / Azure", "System Design", "FinOps"],
        "business_impact": "35% faster architecture sign-off & reduced cloud waste",
        "display_order": 1,
    },
    {
        "slug": "application-development",
        "code": "02 // DEV",
        "title": "Application Development",
        "tagline": "Cloud-Native Full-Stack Platforms, APIs & Microservices",
        "summary": (
            "Design and ship high-throughput, resilient web platforms, asynchronous Python backends, "
            "event-driven microservices, and enterprise portal integrations built for scale."
        ),
        "deliverables": [
            "Custom Web Portals & SaaS Product Engineering",
            "High-Performance REST & GraphQL API Gateways",
            "Legacy Monolith-to-Microservices Refactoring",
            "Automated Testing & Production Release Pipelines",
        ],
        "tech_stack": ["Python", "FastAPI", "Django", "PostgreSQL", "React / HTMX"],
        "business_impact": "Sub-50ms API latency with 99.95% uptime SLA",
        "display_order": 2,
    },
    {
        "slug": "ai-services",
        "code": "03 // AI",
        "title": "AI Services",
        "tagline": "Production LLMs, Enterprise RAG, MCP Servers & Agentic AI",
        "summary": (
            "Move beyond prototypes to governed, auditable Generative AI systems—featuring domain-grounded "
            "RAG pipelines, Model Context Protocol (MCP) tool servers, and multi-agent orchestration."
        ),
        "deliverables": [
            "Enterprise Knowledge RAG & Hybrid Vector Search",
            "Stateful Multi-Agent Workflows (LangGraph)",
            "Custom MCP Servers for Internal ERP/DB Tooling",
            "Predictive Analytics & Quantitative ML Models",
        ],
        "tech_stack": ["LangGraph", "MCP", "Pydantic", "OpenAI / Gemini", "pgvector"],
        "business_impact": "60% reduction in knowledge retrieval & ticket triage time",
        "display_order": 3,
    },
    {
        "slug": "automation",
        "code": "04 // RPA",
        "title": "Automation",
        "tagline": "UiPath RPA Bots, Intelligent Document Processing & Workflow Sync",
        "summary": (
            "Eliminate repetitive back-office operations across finance, HR, and supply chain using "
            "resilient UiPath attended/unattended bots combined with AI-driven document extraction."
        ),
        "deliverables": [
            "End-to-End UiPath Unattended & Attended Bot Suites",
            "Intelligent Document Processing (IDP / OCR) for Invoices",
            "Cross-System SAP, Oracle, Salesforce & Excel Automation",
            "RPA Center of Excellence (CoE) & Bot Monitoring",
        ],
        "tech_stack": ["UiPath Studio", "Orchestrator", "Python", "Document Understanding"],
        "business_impact": "70%+ manual processing hours reclaimed with zero keying errors",
        "display_order": 4,
    },
    {
        "slug": "it-operations",
        "code": "05 // OPS",
        "title": "IT Operations",
        "tagline": "AIOps Observability, Cloud SRE & 24/7 Managed Infrastructure",
        "summary": (
            "Guarantee continuous operational resilience with proactive AIOps anomaly detection, "
            "Infrastructure-as-Code (IaC), zero-downtime CI/CD, and 24/7 SRE incident management."
        ),
        "deliverables": [
            "AIOps Log Correlation & Automated Self-Healing Runbooks",
            "Kubernetes, Docker & Terraform Infrastructure Automation",
            "24/7 L2/L3 Production Support & SLA Governance",
            "Zero-Trust Security Hardening & Disaster Recovery",
        ],
        "tech_stack": ["Docker", "Kubernetes", "Terraform", "Prometheus / Grafana", "Linux"],
        "business_impact": "55% lower Mean Time to Resolution (MTTR)",
        "display_order": 5,
    },
]


async def seed_services(db: AsyncSession) -> None:
    existing = await db.execute(select(ServicePillar.id).limit(1))
    if existing.scalar_one_or_none() is not None:
        return
    for item in RNS_PILLARS:
        db.add(ServicePillar(**item))
    await db.commit()
