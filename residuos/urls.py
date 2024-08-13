from django.urls import path
from .import views

urlpatterns = [
    path('listar/<str:empresa_id>/', views.list, name='listar_residuo'),
    path('add/', views.add, name="adicionar_residuo"),
    path('edit/<int:residuo_id>/', views.edit, name='editar_residuo'),
    path('delete/<int:residuo_id>/', views.delete, name='deletar_residuo'),
]