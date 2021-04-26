from datetime import datetime

import pytz
from django.db import models


class Vuz(models.Model):
 znacka_typ = models.CharField(max_length=100)

 def __str__(self):
  return self.znacka_typ


class Vratka(models.Model):
 jmeno = models.CharField(max_length=100)

 def __str__(self):
  return self.jmeno


@property
def stk(self):
  self.now = datetime.date.today()
  return self.now - self.datum_stk

# Create your models here.
class Auto(models.Model):
 registracni_znacka = models.CharField(max_length=100)
 znacka_typ = models.CharField(max_length=100)
 pocet_km = models.IntegerField()
 datum_stk = models.DateField()
 vuz = models.ForeignKey(Vuz, on_delete=models.SET_NULL, null=True)


class Zakaznik(models.Model):
 programy = (
  ("B", "běžný zákazník"),
  ("Z", "zlatý program"),
  ("P", "platinový program"),
 )
 jmeno = models.CharField(max_length=100)
 prijmeni = models.CharField(max_length=100)
 cislo_prukazu = models.CharField(max_length=100)
 datum_narozeni = models.DateField()
 vratka = models.ForeignKey(Vratka, on_delete=models.SET_NULL, null=True)
 program = models.CharField(max_length=1, choices=programy, null=True)


class Vypujcka(models.Model):
 pocatecni_datum_cas = models.DateTimeField()
 konecne_datum_cas = models.DateTimeField()
 cena = models.IntegerField()
 vratka = models.ForeignKey(Vratka, on_delete=models.SET_NULL, null=True)
 vuz = models.ForeignKey(Vuz, on_delete=models.SET_NULL, null=True)

@property
def state(self):
    self.now = datetime.datetime.now()
    self.now = pytz.utc.localize(self.now)
    if self.now > self.konecne_datum_cas:
      return("Výpůjčka již proběhla.")
    elif self.now >= self.pocatecni_datum_cas:
      return("Výpůjčka probíhá.")
    elif self.now < self.pocatecni_datum_cas:
      return("Výpůjčka ještě neproběhla.")