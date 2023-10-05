from .models import Stand, Reserva
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm


def index(request):
    total_stand = Stand.objects.count()
    total_reserva = Reserva.objects.count()
    return render(request, "core/index.html", {'total_stand': total_stand, 'total_reserva': total_reserva})


def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm()
    return render(request, "core/reserva_form.html", {'form': form})


def reservas(request):
    reservas = Reserva.objects.all()
    return render(request, "core/reservas.html", {'reservas': reservas})


def reserva_detalhe(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    return render(request, "core/reserva_detalhe.html", {'reserva': reserva})


def reserva_editar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'core/reserva_form.html', {'form': form})


def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reservas')
