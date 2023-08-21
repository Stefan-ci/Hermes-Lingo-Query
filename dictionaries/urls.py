from dictionaries import views
from django.urls import path

app_name = "dictionaries"

urlpatterns = [
    path("", views.DictionaryApiView.as_view(), name="search-word"),
]
