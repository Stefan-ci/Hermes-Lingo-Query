from core import views
from django.urls import path, re_path
from core.docs import api_documentation_view

app_name = "core"


urlpatterns = [
    path("", views.home_view, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("profile/", views.profile_view, name="profile"),
    path("logout/", views.logout_view, name="logout"),
]


urlpatterns += [
    path("api/docs/", api_documentation_view.with_ui("redoc", cache_timeout=0), name="api-schema-redoc"),
    path("api/docs/ui/", api_documentation_view.with_ui("swagger", cache_timeout=0), name="api-schema-swagger-ui"),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", api_documentation_view.without_ui(cache_timeout=0), name="api-schema-json"),
]
