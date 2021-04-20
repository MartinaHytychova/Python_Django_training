from django.shortcuts import render

from django.views.generic import ListView
from . import models

class KurzyView(ListView):
    model = models.Kurz
    template_name = "kurzy/kurzy_list.html"