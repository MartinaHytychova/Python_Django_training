from django.urls import path
from . import views

urlpatterns = [
    path('kurzy/', views.KurzyView.as_view(), name='kurzy'),
]
