from django.db import models
from parki.models import Sektor
# Create your models here.
statusy = [
    ('Otwarty', 'Otwarty'),
    ('Zamkniety', 'Zamknięty')
]

class Atrakcja(models.Model):
    nazwa = models.CharField(max_length=30)
    producent = models.CharField(max_length=30)
    typ_atrakcji = models.CharField(max_length=30)
    opis = models.CharField(max_length=400)
    wymagania_wiekowe = models.IntegerField()
    status = models.CharField(max_length=30, choices=statusy)
    wysokosc = models.IntegerField(null=True)
    predkosc = models.IntegerField(null=True)
    przeciazenie = models.IntegerField(null=True)
    przepustowosc = models.IntegerField(null=True)
    dlugosc_trasy = models.IntegerField(null=True)
    data_przegladu = models.DateField(null=True)
    waznosc_przegladu = models.DateField(null=True)
    id_sektora = models.ForeignKey(Sektor, on_delete=models.CASCADE)

