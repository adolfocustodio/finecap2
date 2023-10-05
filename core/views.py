from .models import Stand, Reserva
from django.shortcuts import render


def index(request):
    total_stand = Stand.objects.count()
    total_reserva = Reserva.objects.count()
    return render(request, "core/index.html", {'total_stand': total_stand, 'total_reserva': total_reserva})
