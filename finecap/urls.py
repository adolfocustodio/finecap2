from django.urls import path
from core.views import *
from django.contrib import admin


urlpatterns = [
    path('', index, name='index'),
    path('reserva/criar', reserva_criar, name='reserva_criar'),
    path('reservas', reservas, name='reservas'),
    path('reserva/detalhe/<int:id>', reserva_detalhe, name='reserva_detalhe'),
    path('reserva/editar/<int:id>', reserva_editar, name='reserva_editar'),
    path('reserva/remover/<int:id>', reserva_remover, name='reserva_remover'),
    path('admin/', admin.site.urls)
]
