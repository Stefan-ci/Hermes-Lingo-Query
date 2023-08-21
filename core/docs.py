from drf_yasg import openapi
from django.conf import settings
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from rest_framework.authentication import BasicAuthentication, TokenAuthentication


api_documentation_view = get_schema_view(
    openapi.Info(
        title=f"{settings.SITE_NAME} API Docs",
        default_version="1.0",
        description="",
        terms_of_service="",
        contact=openapi.Contact(email="s.diby@waliye.com", name="K. Stéphane Claver DIBY"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
    authentication_classes=[BasicAuthentication, TokenAuthentication]
)
