from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('lista_perritos/', views.lista_perritos, name='lista_perritos'),
    path('lista_perritos/<int:id>/', views.detalle_perrito, name='detalle_perrito'),
    path('cuidadores/', views.cuidadores, name='cuidadores'),
    path('veterinarias/', views.vets, name='veterinarias'),
    path('donaciones/', views.money, name='donaciones')



]
