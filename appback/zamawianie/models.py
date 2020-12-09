from django.db import models
from parki.models import PunktSprzedazy, ParkRozrywki

# Create your models here.
class Rabat(models.Model):
    nazwa = models.CharField(max_length=30)
    wartosc = models.DecimalField(max_digits=4, decimal_places=2)


class Bilet(models.Model):
    nazwa = models.CharField(max_length=30)
    czy_rabat = models.BooleanField(default=False)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    id_rabatu = models.ForeignKey(Rabat, on_delete=models.CASCADE)
    id_punktu_sprzedazy = models.ForeignKey(PunktSprzedazy, on_delete=models.CASCADE)


class Klient(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    nr_telefonu = models.CharField(max_length=13)
    id_parku_rozrywki = models.ForeignKey(ParkRozrywki, on_delete=models.CASCADE)


class Zamowienie(models.Model):
    id_biletu = models.ForeignKey(Bilet, on_delete=models.CASCADE)
    id_klienta = models.ForeignKey(Klient, on_delete=models.CASCADE)
    data_zakupy = models.DateTimeField(auto_now_add=True)
    data_aktywacji = models.DateTimeField()
    data_waznosci = models.DateTimeField()



