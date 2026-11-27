from django.http import Http404
from django.shortcuts import render
from app.services.backend_client import BackendClient


def home_view(request):
    services = BackendClient.get_services()
    return render(
        request,
        "home.html",
        {
            "page_title": "Rise Nest Solutions",
            "services": services,
        },
    )


def service_detail_view(request, slug: str):
    service = BackendClient.get_service_by_slug(slug)
    if not service:
        raise Http404("Practice area not found")
    all_services = BackendClient.get_services()
    return render(
        request,
        "service_detail.html",
        {
            "page_title": f"{service['title']} | Rise Nest Solutions",
            "service": service,
            "all_services": all_services,
        },
    )


def contact_view(request):
    selected_slug = request.GET.get("service", "consultancy")
    services = BackendClient.get_services()
    receipt = None
    error_message = None

    form_data = {
        "full_name": "",
        "work_email": "",
        "company_name": "",
        "phone": "",
        "service_slug": selected_slug,
        "project_scope": "",
    }

    if request.method == "POST":
        form_data = {
            "full_name": request.POST.get("full_name", "").strip(),
            "work_email": request.POST.get("work_email", "").strip(),
            "company_name": request.POST.get("company_name", "").strip(),
            "phone": request.POST.get("phone", "").strip() or None,
            "service_slug": request.POST.get("service_slug", "consultancy").strip(),
            "project_scope": request.POST.get("project_scope", "").strip(),
        }
        ok, result = BackendClient.create_inquiry(form_data)
        if ok:
            receipt = result
        else:
            error_message = result.get("detail")

    return render(
        request,
        "contact.html",
        {
            "page_title": "Contact Us | Rise Nest Solutions",
            "services": services,
            "form_data": form_data,
            "receipt": receipt,
            "error_message": error_message,
        },
    )

def about_us_view(request):
    return render(request, 'about.html')