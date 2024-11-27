from django.shortcuts import render
from .models import Perrito
from django.shortcuts import get_object_or_404

#vista para perritos

def inicio(request):
    return render(request, 'perritos/inicio.html')

def lista_perritos(request):
    perritos = Perrito.objects.filter(disponible=True)
    return render(request, 'perritos/lista_perritos.html', {'perritos': perritos})

#Perfil perrito

def detalle_perrito(request, id):
    perrito = get_object_or_404(Perrito, id=id)
    return render(request, 'perritos/detalle_perrito.html', {'perrito': perrito})

#vista para veterinarias

def vets(request):
    return render(request,'perritos/vets.html')

#vista para cuidadores

def cuidadores(request):
    return render(request,'perritos/cuidadores.html')

#vista para donaciones

def money(request):
    return render(request,'perritos/money.html')
