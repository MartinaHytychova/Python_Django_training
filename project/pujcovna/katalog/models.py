from django.db import models

# Create your models here.
class Auto(models.Model):
 registracni_znacka = models.CharField(max_length=100)
 znacka_typ = models.CharField(max_length=100)
 pocet_km = models.IntegerField()
 datum_stk = models.DateField()

class Zakaznik(models.Model):
 jmeno = models.CharField(max_length=100)
 prijmeni = models.CharField(max_length=100)
 cislo_prukazu = models.CharField(max_length=100)
 datum_narozeni = models.DateField()

class Vypujcka(models.Model):
 pocatecni_datum_cas = models.DateTimeField()
 konecne_datum_cas = models.DateTimeField()
 cena = models.IntegerField()