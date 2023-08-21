"""
URL configuration for hermes_lingo_query project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.views.static import serve
from django.conf.urls.static import static

API_BASE_URL = "api"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("rest/framework/", include("rest_framework.urls")),
    
    path("", include("core.urls", namespace="core")),
    
    path(f"{API_BASE_URL}/accounts/", include("accounts.urls", namespace="accounts")),
    path(f"{API_BASE_URL}/dictionary/", include("dictionaries.urls", namespace="dictionaries")),
    path(f"{API_BASE_URL}/translate/", include("translations.urls", namespace="translations")),
]


urlpatterns += static(settings.STATIC_URL, serve, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, serve, document_root=settings.MEDIA_ROOT)
