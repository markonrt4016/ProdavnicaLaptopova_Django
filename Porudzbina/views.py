from django.shortcuts import render

# Create your views here.


from Korpa.korpa import Korpa
from .models import StavkaPorudzbine
from .forms import FormaZaPorudzbinu

def KreiranjePorudzbine(request):
    korpa = Korpa(request)
    print('usao')

    ##test:

    if request.user.is_authenticated:
        print(request.user.username)

    ##kraj testa

    if request.method == 'POST':
        forma = FormaZaPorudzbinu(request.POST)

        if forma.is_valid():
            porudzbina = forma.save()

            for stavka in korpa:
                StavkaPorudzbine.objects.create(porudzbina=porudzbina, laptop=stavka['laptop'], cena=stavka['cena'], kolicina=stavka['kolicina'])

            korpa.ObrisiJeIzSesije()

            return render(request, 'Porudzbina/created.html', {'porudzbina': porudzbina})

    else:
        forma = FormaZaPorudzbinu()
    print('dosao vodje')
    return render(request, 'Porudzbina/create.html', {'korpa': korpa, 'forma': forma})


