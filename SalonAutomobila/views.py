from django.shortcuts import render, get_object_or_404
from .models import Segment,Automobil

def ListaAutomobila(request, segment_slug = None):
    segment = None
    segmenti = Segment.objects.all()
    automobili = Automobil.objects.filter(raspoloziv=True)
    if segment_slug:
        segment = get_object_or_404(Segment, slug=segment_slug)
        automobili = automobili.filter(segment=segment)

    return render(request, 'SalonAutomobila/automobili/list.html', {'segment': segment, 'segmenti': segmenti, 'automobili': automobili})

def DetaljiAutomobila(request,id,slug):
    automobil = get_object_or_404(Automobil, id=id, slug = slug, raspoloziv = True)

    return render(request, 'SalonAutomobila/automobili/detail.html', {'automobil': automobil})


