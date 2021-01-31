from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from ProdavnicaLaptopova.models import Laptop
from .korpa import Korpa
from .forms import FormaZaDodavanjeLaptopaUKorpu

@require_POST
def DodajUKorpu(request, laptop_id):
    print('usao')
    korpa = Korpa(request)
    laptop = get_object_or_404(Laptop, id=laptop_id)
    form = FormaZaDodavanjeLaptopaUKorpu(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        korpa.Dodaj(laptop=laptop, kolicina=cd['kolicina'], dodati_na_kolicinu=cd['dodati_na_kolicinu'])
    print('prosao')
    print(laptop)

    return redirect('Korpa:DetaljiKorpe')

@require_POST
def UkloniIzKorpe(request, laptop_id):
    korpa = Korpa(request)
    laptop = get_object_or_404(Laptop, id=laptop_id)
    korpa.Ukloni(laptop)
    return redirect('Korpa:DetaljiKorpe')


def DetaljiKorpe(request):
    korpa = Korpa(request)
    for stavka in korpa:
        stavka['formazaazuriranjekolicine'] = FormaZaDodavanjeLaptopaUKorpu(initial={'kolicina': 1, 'dodati_na_kolicinu': True})
    print('valja renderovat')
    return render(request, 'Korpa/detail.html', {'korpa': korpa})









