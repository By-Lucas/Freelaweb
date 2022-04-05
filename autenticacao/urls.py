from django.urls import path, include
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),
    path('sair/', views.sair, name="sair")
]