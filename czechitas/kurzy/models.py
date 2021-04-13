from django.db import models

# Create your models here.
class Kurz(models.Model):
  nazev = models.CharField(max_length=100)
  zacatek = models.DateTimeField()
  konec = models.DateTimeField()
  popis = models.CharField(max_length=1000)
  cena = models.IntegerField()
  cena = models.IntegerField()