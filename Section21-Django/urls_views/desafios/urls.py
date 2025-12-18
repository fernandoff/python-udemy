from django.urls import path
from .views import desafio_semana, desafio_semana_numero, index

urlpatterns = [
    path('', index, name='index'),
    path('<int:dia>', desafio_semana_numero),
    path('<str:dia>', desafio_semana, name='desafio_semanal')
]
