# Rise Nest Solutions (RNS) — Enterprise Platform Architecture

## 1. Project Overview & Architecture
Rise Nest Solutions (RNS) is a decoupled two-tier Python enterprise web application covering five core practice pillars:
1. **Consultancy**: Enterprise architecture blueprints, cloud modernization roadmaps, and ROI audits.
2. **Application Development**: Cloud-native web platforms, high-throughput REST APIs, and microservices.
3. **AI Services**: Production LLMs, domain-grounded RAG pipelines, Model Context Protocol (MCP) servers, and LangGraph agents.
4. **Automation**: UiPath attended/unattended RPA bots, Intelligent Document Processing (IDP/OCR), and ERP/CRM workflow sync.
5. **IT Operations**: AIOps observability, Infrastructure-as-Code (IaC), CI/CD pipelines, and 24/7 SRE support.

## 2. System Topology
`Browser` ──(HTTP / HTML)──▶ `Frontend Django 5.2 LTS (Port 8001)` ──(REST JSON via httpx)──▶ `Backend FastAPI + SQLAlchemy Async (Port 8000)` ──▶ `SQLite / PostgreSQL`

## 3. Quick Start
### Backend (`RNS/backend/`)
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env
pytest
uvicorn app.main:app --reload --port 8000
```

### Frontend (`RNS/frontend/`)
```bash
cd frontend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py runserver 8001
```
