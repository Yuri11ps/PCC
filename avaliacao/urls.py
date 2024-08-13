from django.urls import path
from .import views

urlpatterns = [
    path('<str:empresa_id>/', views.list, name='listar_avaliacao'),
    path("add/<str:empresa_id>/", views.add, name="adicionar_avaliacao"),
    path('edit/<int:avaliacao_id>/', views.edit, name='editar_avaliacao'),
    path('delete/<int:avaliacao_id>/', views.delete, name='deletar_avaliacao'),
]