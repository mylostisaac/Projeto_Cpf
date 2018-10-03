from django.urls import path

from . import views

app_name = 'cpf'

urlpatterns = [

    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('vote/', views.vote, name='vote'),
    path('<int:question_id>/voltar/', views.voltar, name='voltar'),
    path('validate', views.validateCpf, name='validate'),
    path('generate', views.generateCpf, name='generate'),
]