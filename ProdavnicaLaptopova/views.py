from django.shortcuts import render, get_object_or_404
from .models import Segment,Laptop

from Korpa.forms import FormaZaDodavanjeLaptopaUKorpu
from Korpa.korpa import Korpa

def ListaLaptopova(request, segment_slug = None):
    segment = None
    segmenti = Segment.objects.all()
    laptopovi = Laptop.objects.filter(raspoloziv=True)
    if segment_slug:
        segment = get_object_or_404(Segment, slug=segment_slug)
        laptopovi = laptopovi.filter(segment=segment)
    korpa = Korpa(request)
    return render(request, 'ProdavnicaLaptopova/laptopovi/list.html', {'segment': segment, 'segmenti': segmenti, 'laptopovi': laptopovi, 'korpa':korpa})

def DetaljiLaptopa(request, id, slug):
    laptop = get_object_or_404(Laptop, id=id, slug = slug, raspoloziv = True)

    korpa = Korpa(request)
    formazadodavanjelaptopaukorpu = FormaZaDodavanjeLaptopaUKorpu()

    return render(request, 'ProdavnicaLaptopova/laptopovi/detail.html', {'laptop': laptop, 'formazadodavanjelaptopaukorpu': formazadodavanjelaptopaukorpu, 'korpa': korpa})


