from django.db import models

class Kategorie(models.Model):
  nazev = models.CharField(max_length=100)

  def __str__(self):
    return self.nazev

# Create your models here.
class Kurz(models.Model):
  nazev = models.CharField(max_length=100)
  zacatek = models.DateTimeField()
  konec = models.DateTimeField()
  popis = models.CharField(max_length=1000)
  cena = models.IntegerField()
  kategorie = models.ForeignKey(Kategorie, on_delete=models.SET_NULL, null=True)
