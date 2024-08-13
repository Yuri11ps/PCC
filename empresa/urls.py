from django.urls import path
from .import views

urlpatterns = [
    path('', views.list, name='listar_empresa'),
    path("add/", views.add, name="adicionar_empresa"),
    path('edit/<int:empresa_id>/', views.edit, name='editar_empresa'),
    path('delete/<int:empresa_id>/', views.delete, name='deletar_empresa'),
]


