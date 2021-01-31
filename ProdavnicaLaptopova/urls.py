from django.urls import path
from . import views

app_name = 'prodavnicalaptopova'

urlpatterns = [path('', views.ListaLaptopova, name='ListaLaptopova'), path('<slug:segment_slug>/', views.ListaLaptopova, name='ListaLaptopovaPoSegmentu'), path('<int:id>/<slug:slug>/', views.DetaljiLaptopa, name='DetaljiLaptopa')]
