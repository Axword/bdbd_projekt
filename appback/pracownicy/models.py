from django.db import models
from parki.models import Adres, ParkRozrywki

# Create your models here.
class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=30, unique=True)
    opis = models.CharField(max_length=400)


class Pracownik(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    data_urodzenia = models.DateField(auto_now=False, auto_now_add=False)
    pesel = models.CharField(max_length=13, null=True, unique=True)
    email = models.CharField(max_length=30, unique=True)
    nr_telefonu = models.CharField(max_length=13, unique=True)
    nr_konta_bankowego = models.CharField(max_length=26, unique=True)
    data_zatrudnienia = models.DateField()
    data_zwolnienia = models.DateField(null=True)
    id_parku_rozrywki = models.ForeignKey(ParkRozrywki, on_delete=models.CASCADE)
    id_adresu = models.ForeignKey(Adres, on_delete=models.CASCADE)
    id_stanowiska = models.ForeignKey(Stanowisko, on_delete=models.CASCADE)


class Wynagrodzenie(models.Model):
    data_wynagrodzenia = models.DateField()
    kwota_podstawowa = models.DecimalField(max_digits=10, decimal_places=2)
    kwota_dodatkowa = models.DecimalField(max_digits=10, decimal_places=2)
    id_pracownika = models.ForeignKey(Pracownik, on_delete=models.CASCADE)


class Wlasciciel(models.Model):
    imie = models.CharField(max_length=30)
    nazwisko = models.CharField(max_length=30)
    id_parku_rozrywki = models.ForeignKey(ParkRozrywki, on_delete=models.CASCADE)
    id_adresu = models.ForeignKey(Adres, on_delete=models.CASCADE)
