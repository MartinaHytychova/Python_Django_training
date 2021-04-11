from django.urls import path
from . import views

urlpatterns = [
    path("katalog", views.IndexView.as_view(), name="katalog"),
    path("katalog/seznam", views.SeznamView.as_view(), name="seznam")
]
