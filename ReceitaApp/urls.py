from django.urls import path
from ReceitaApp import views

urlpatterns = [
        #caminho,    #view Correspondente, name da url
    path('', views.index, name='index'),
    path('receitas/', views.listar_receitas, name='receitas'),
]

#para cada url do site, coloco uma linha nessa lista urlpatterns