from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from . import models


class IndexView(View):
  def get(self, request):
    return HttpResponse("<h1>Autopůjčovna</h1>"
                        "<a href='http://localhost:8000/katalog/auto/'>Seznam aut</a><br>"
                        "<a href='http://localhost:8000/katalog/vypujcka/'>Seznam výpůjček</a><br>"
                        "<a href='http://localhost:8000/katalog/zakaznik/'>Seznam zákazníků</a><br>"
                        )

class AutoView(ListView):
    model = models.Auto
    template_name = "katalog/seznam_aut.html"


class VypujckaView(ListView):
    model = models.Vypujcka
    template_name = "katalog/prehled_vypujcek.html"


class ZakaznikView(ListView):
  model = models.Zakaznik
  template_name = "katalog/zakaznici.html"