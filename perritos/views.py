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



