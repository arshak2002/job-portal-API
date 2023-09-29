from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/accounts/",include('apps.accounts.urls')),
    path("api/company/",include('apps.company.urls')),
    path("api/employee/",include('apps.employee.urls')),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/",
        SpectacularSwaggerView.as_view(url="/schema/?format=json", url_name="schema"),
        name="swagger-ui",
    ),
    path("redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
