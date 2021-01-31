from decimal import Decimal
from django.conf import settings
from ProdavnicaLaptopova.models import Laptop

class Korpa(object):
    def __init__(self, request):
        self.sesija = request.session
        korpa = self.sesija.get(settings.KORPA_ZA_KUPOVINU_SESSION_KEY)
        if not korpa:
            korpa = self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY] = {}

        self.korpa = korpa

    def __iter__(self):
        laptopovi_ids = self.korpa.keys()
        laptopovi = Laptop.objects.filter(id__in=laptopovi_ids)
        korpakopija = self.korpa.copy()

        for laptop in laptopovi:
            korpakopija[str(laptop.id)]['laptop'] = laptop

        for stavka in korpakopija.values():
            stavka['cena'] = Decimal(stavka['cena'])
            stavka['ukupna_cena'] = stavka['cena'] * stavka['kolicina']
            yield stavka

    def __len__(self):
        return sum(stavka['kolicina'] for stavka in self.korpa.values())

    def Dodaj(self, laptop, kolicina=1, dodati_na_kolicinu=True):
        laptop_id = str(laptop.id)

        if laptop_id not in self.korpa:
            self.korpa[laptop_id] = {'kolicina':0, 'cena': str(laptop.cena)}

        if dodati_na_kolicinu:
            self.korpa[laptop_id]['kolicina'] += kolicina
        else:
            self.korpa[laptop_id]['kolicina'] = kolicina

        self.sesija.modified = True

    def Ukloni(self, laptop):
        laptop_id = str(laptop.id)
        if laptop_id in self.korpa:
            del self.korpa[laptop_id]
            self.sesija.modified=True

    def ObrisiJeIzSesije(self):
        del self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY]
        self.sesija.modified = True

    def UzmiUkupnuCenu(self):
        return sum(Decimal(stavka['cena']) * stavka['kolicina'] for stavka in self.korpa.values())

