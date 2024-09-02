from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('buscar/', views.buscar_socio, name='buscar_socio'),
    path('salvar/', views.salvar_busca, name='salvar_busca'),
    path('relatorio_uf', views.relatorio_uf, name="relatorio_uf"),
    path('relatorio_data', views.relatorio_data, name="relatorio_data")
]
