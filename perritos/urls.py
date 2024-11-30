from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('lista_perritos/', views.lista_perritos, name='lista_perritos'),
    path('lista_perritos/<int:id>/', views.detalle_perrito, name='detalle_perrito'),
    path('cuidadores/', views.cuidadores, name='cuidadores'),
    path('veterinarias/', views.listar_veterinarias, name='veterinarias'),
    path('<int:id>/', views.detalle_veterinaria, name='detalle_veterinaria'),
    path('donaciones/', views.money, name='donaciones'),
    path('lista_cuidadores/', views.lista_cuidadores, name='lista_cuidadores'),
    path('lista_cuidadores/<int:cuidador_id>/', views.detalle_cuidador, name='detalle_cuidador')
]
