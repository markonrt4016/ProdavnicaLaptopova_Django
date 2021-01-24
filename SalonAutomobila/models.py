from django.db import models
from django.urls import reverse
# Create your models here.

class Segment(models.Model):
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('naziv',)
        verbose_name = 'segment'
        verbose_name_plural = 'segmenti'

    def __str__(self):
        return self.naziv

    def ApsolutniURL(self):
        return reverse('SalonAutomobila:ListaAutomobilaPoSegmentu', args=[self.slug])


class Automobil(models.Model):
    segment = models.ForeignKey(Segment, related_name='automobili', on_delete=models.CASCADE)
    naziv = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    slika = models.ImageField(upload_to='automobili/%Y/%m/%d', blank=True)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=10,decimal_places=2)
    raspoloziv = models.BooleanField(default=True)
    kreiran = models.DateTimeField(auto_now_add=True)
    azuriran = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('naziv',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'automobili'

    def __str__(self):
        return self.naziv
    def ApsolutniURL(self):
        return reverse('SalonAutomobila:DetaljiAutomobila', args=[self.id, self.slug])