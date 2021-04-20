from django.urls import path
from . import views

urlpatterns = [
    path('kontakty/', views.KontaktView.as_view(), name='kontakty'),
    path('organizace/', views.OrganizaceView.as_view(), name='organizace'),
]
