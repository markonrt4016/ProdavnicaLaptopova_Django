from decimal import Decimal
from django.conf import settings
from SalonAutomobila.models import Automobil

class Korpa(object):
    def __init__(self, request):
        self.sesija = request.session
        korpa = self.sesija.get(settings.KORPA_ZA_KUPOVINU_SESSION_KEY)
        if not korpa:
            korpa = self.sesija[settings.KORPA_ZA_KUPOVINU_SESSION_KEY] = {}

        self.korpa = korpa

    def __iter__(self):
        automobili_ids = self.korpa.keys()
        automobili = Automobil.objects.filter(id__in=automobili_ids)
        korpakopija = self.korpa.copy()

        for automobil in automobili:
            korpakopija[str(automobil.id)]['automobil'] = automobil

        for stavka in korpakopija.values():
            stavka['cena'] = Decimal(stavka['cena'])
            stavka['ukupna_cena'] = stavka['cena'] * stavka['kolicina']
            yield stavka

    def __len__(self):
        return sum(stavka['kolicina'] for stavka in self.korpa.values())

    def Dodaj(self, automobil, kolicina=1, dodati_na_kolicinu=True):
        automobil_id = str(automobil.id)

        if automobil_id not in self.korpa:
            self.korpa[automobil_id] = {'kolicina':0, 'cena': str(automobil.cena)}

        if dodati_na_kolicinu:
            self.korpa[automobil_id]['kolicina'] += kolicina
        else:
            self.korpa[automobil_id]['kolicina'] = kolicina

        self.sesija.modified = True

    def Ukloni(self, automobil):
        automobil_id = str(automobil.id)
        if automobil_id in self.korpa:
            del self.korpa[automobil_id]
            self.sesija.modified=True

    def ObrisiJeIzSesije(self):
        del self.sesija[settings.KORPA_ZA_KUPOVINU_SESION_KEY]
        self.sesija.modified = True

    def UzmiUkupnuCenu(self):
        return sum(Decimal(stavka['cena']) * stavka['kolicina'] for stavka in self.korpa.values())

