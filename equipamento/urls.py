from django.urls import path
from .import views

urlpatterns = [
    path('<str:empresa_id>/', views.list, name='listar_equipamento'),
    path('add/<str:empresa_id>/', views.add, name="adicionar_equipamento"),
    path('edit/<int:equipamento_id>/', views.edit, name='editar_equipamento'),
    path('delete/<int:equipamento_id>/', views.delete, name='deletar_equipamento'),
]