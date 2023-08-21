from django.urls import path
from translations import views

app_name = "translations"

urlpatterns = [
    path("", views.TranslatorApiView.as_view(), name="translate-sentence"),
]
