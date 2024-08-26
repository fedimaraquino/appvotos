from django.urls import path
from . import views

urlpatterns = [
    path('secoes/', views.secao_list, name='secao_list'),
    path('secoes/adicionar/', views.secao_create, name='secao_create'),
    path('secoes/<int:id>/editar/', views.secao_update, name='secao_update'),
    path('secoes/<int:id>/excluir/', views.secao_delete, name='secao_delete'),

    path('usuarios/', views.usuario_list, name='usuario_list'),
    path('usuarios/adicionar/', views.usuario_create, name='usuario_create'),
    path('usuarios/<int:id>/editar/', views.usuario_update, name='usuario_update'),
    path('usuarios/<int:id>/excluir/', views.usuario_delete, name='usuario_delete'),

    path('candidatos/', views.candidato_list, name='candidato_list'),
    path('candidatos/adicionar/', views.candidato_create, name='candidato_create'),
    path('candidatos/<int:id>/editar/', views.candidato_update, name='candidato_update'),
    path('candidatos/<int:id>/excluir/', views.candidato_delete, name='candidato_delete'),

    path('cargos/', views.cargo_list, name='cargo_list'),
    path('cargos/adicionar/', views.cargo_create, name='cargo_create'),
    path('cargos/<int:id>/editar/', views.cargo_update, name='cargo_update'),
    path('cargos/<int:id>/excluir/', views.cargo_delete, name='cargo_delete'),
    path('registrar-resultados/', views.registrar_resultados, name='registrar_resultados'),
    #path('resultados-registrados/', views.resultados_registrados, name='resultados_registrados'),
    path('dashboard/', views.dashboard, name='dashboard'),
    #path('dashboard/', views.dashboard, name='dashboard'),
    path('resultados-registrados/', views.resultados_registrados, name='resultados_registrados'),
]

