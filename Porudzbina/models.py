from django.db import models
from ProdavnicaLaptopova.models import Laptop


class Porudzbina(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    email = models.EmailField()
    adresa = models.CharField(max_length=250)
    postanski_broj = models.CharField(max_length=20)
    grad = models.CharField(max_length=100)
    datum_kreiranja = models.DateTimeField(auto_now_add=True)
    datum_azuriranja = models.DateTimeField(auto_now=True)
    placeno = models.BooleanField(default=True)

    class Meta:
        ordering = ('-datum_kreiranja',)
        verbose_name = 'porudzbina'
        verbose_name_plural = 'porudzbine'

    def __str__(self):
        return f'Porudzbina {self.id}'

    def UzmiUkupnuCenuPorudzbine(self):
        return sum(stavka.UzmiCenu() for stavka in self.stavka_porudzbine_p.all())


class StavkaPorudzbine(models.Model):
    porudzbina = models.ForeignKey(Porudzbina,
                                   related_name='stavke_porudzbine_p',
                                   on_delete=models.CASCADE)
    laptop = models.ForeignKey(Laptop,
                                  related_name='stavke_porudzbine_a',
                                  on_delete=models.CASCADE)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    kolicina = models.PositiveIntegerField(default=1)

    def __str__(self): return str(self.id)

    def UzmiCenu(self): return self.cena * self.kolicina
