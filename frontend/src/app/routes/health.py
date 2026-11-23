from django.http import JsonResponse
from app.services.health_service import check_platform_health


def health_view(request):
    return JsonResponse(check_platform_health())
