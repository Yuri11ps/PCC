from django.urls import path
from .import views

urlpatterns = [
    path('id/<str:empresa_id>/', views.list, name='listar_rota'),
    path('mapa/', views.listMap, name='listar_mapa_rota'),
    path('add/<str:empresa_id>/', views.add, name="adicionar_rota"),
    path('edit/<int:rota_id>/', views.edit, name='editar_rota'),
    path('delete/<int:rota_id>/', views.delete, name='deletar_rota'),
]