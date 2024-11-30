from django.shortcuts import render
from .models import Perrito
from .models import Veterinaria
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



def listar_veterinarias(request):
    veterinarias = Veterinaria.objects.all()  # Consulta todas las veterinarias
    return render(request, 'perritos/vets.html', {'veterinarias': veterinarias})

def detalle_veterinaria(request, id):
    veterinaria = get_object_or_404(Veterinaria, id=id)
    return render(request, 'perritos/detalle_vet.html', {'veterinaria': veterinaria})

#vista para cuidadores

def cuidadores(request):
    return render(request,'perritos/cuidadores.html')

#vista para donaciones

def money(request):
    return render(request,'perritos/money.html')
