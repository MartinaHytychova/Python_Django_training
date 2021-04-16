from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("katalog", views.IndexView.as_view(), name="katalog"),
    path("katalog/seznam", views.SeznamView.as_view(), name="seznam")
]
