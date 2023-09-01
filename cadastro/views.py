from django.shortcuts import render, get_object_or_404, redirect
from .form import ReservaForm
from .models import Reserva, Stand
# Create your views here.

def reserva_editar(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReservaForm(instance=reserva)

    return render(request, 'cadastro/form.html', {'form': form})

def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('index')

def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    
    else:
        form = ReservaForm()

    return render(request, 'cadastro/form.html', {'form': form})

def index(request):
    reservas = Reserva.objects.all()
    context = {'reservas': reservas}
    return render(request, 'cadastro/index.html', context)

def reserva_detalhar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {'reserva': reserva}

    return render(request, 'cadastro/detalhe_reserva.html', context)

