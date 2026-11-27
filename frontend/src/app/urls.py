from django.urls import path
from app.routes.health import health_view
from app.routes.views import contact_view, home_view, service_detail_view

urlpatterns = [
    path("", home_view, name="home"),
    path("services/<slug:slug>/", service_detail_view, name="service_detail"),
    #path("industries/", health_view, name="industries"),
    path("health/", health_view, name="health"),
    path("contact/", contact_view, name="contact"),
]
