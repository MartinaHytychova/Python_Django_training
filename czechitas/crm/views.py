from django.shortcuts import render

from django.views.generic import ListView
from . import models

class KontaktView(ListView):
    model = models.Kontakt
    template_name = "crm/kontakty_list.html"

class OrganizaceView(ListView):
    model = models.Organizace
    template_name = "crm/organizace_list.html"