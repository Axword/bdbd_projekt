from django.db import models

# Create your models here.

statusy = [
    ('Otwarty', 'Otwarty'),
    ('Zamkniety', 'Zamknięty')
]
class Adres(models.Model):
    miasto = models.CharField(max_length=30)
    ulica = models.CharField(max_length=30)
    nr_lokalu = models.CharField(max_length=30)
    kod_pocztowy = models.CharField(max_length=30)

class ParkRozrywki(models.Model):
    nazwa = models.CharField(max_length=30)
    data_zalozenia = models.DateField()
    id_adresu = models.ForeignKey(Adres, on_delete=models.CASCADE)


class Sektor(models.Model):
    nazwa = models.CharField(max_length=30)
    status = models.CharField(max_length=30, choices=statusy)
    opis = models.CharField(max_length=400)
    data_zalozenia = models.DateField()
    id_parku_rozrywki = models.ForeignKey(ParkRozrywki, on_delete=models.CASCADE)


class PunktSprzedazy(models.Model):
    nazwa = models.CharField(max_length=30)
    liczba_kas = models.IntegerField()
    status = models.CharField(max_length=30, choices=statusy)
    id_parku_rozrywki = models.ForeignKey(ParkRozrywki, on_delete=models.CASCADE)