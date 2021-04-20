from django.db import models

class Kategorie(models.Model):
  nazev = models.CharField(max_length=100)

  def __str__(self):
    return self.nazev

# Create your models here.
class Kontakt(models.Model):
  jmeno = models.CharField(max_length=100)
  prijmeni = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  datum = models.DateTimeField()
  kategorie = models.ForeignKey(Kategorie, on_delete=models.SET_NULL, null=True)

class Organizace(models.Model):
  nazev = models.CharField(max_length=100)
  ico = models.IntegerField()
  ulice = models.CharField(max_length=100)
  mesto = models.CharField(max_length=100)
  psc = models.IntegerField()
  kategorie = models.ForeignKey(Kategorie, on_delete=models.SET_NULL, null=True)

