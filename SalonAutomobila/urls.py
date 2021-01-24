from django.urls import path
from . import views

app_name = 'salonautomobila'

urlpatterns = [path('', views.ListaAutomobila, name='ListaAutomobila'), path('<slug:segment_slug>/', views.ListaAutomobila, name='ListaAutomobilaPoSegmentu'), path('<int:id>/<slug:slug>/', views.DetaljiAutomobila, name='DetaljiAutomobila')]
