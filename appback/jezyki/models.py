from django.db import models

# Create your models here.

class Jezyk(models.Model):
    kod_jezyka = models.CharField(max_length=2, unique=True)
    nazwa = models.CharField(max_length=20)


class PoziomJezyka(models.Model):
    kody_poziomow = [
        ('A1', 'Poziom A1'),
        ('A2', 'Poziom A2'),
        ('B1', 'Poziom B1'),
        ('B2', 'Poziom B2'),
        ('C1', 'Poziom C1'),
        ('C2', 'Poziom C2')
    ]
    kod_poziomu = models.CharField(max_length=2, choices=kody_poziomow)
    opis = models.CharField(max_length=800)