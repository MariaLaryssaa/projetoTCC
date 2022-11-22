from django.urls import path
from .views import *

urlpatterns = [
    path('', TCCList.as_view(), name='index'),
    path('dashboard/tcc/', TCCListPorUsuario.as_view(), name='listar_tcc_usuario'),
    path('listar/tcc_autor/<int:autor>/', TCCAutorList.as_view(), name='listar_tcc_autor'),
    path('listar/tcc_curso/<int:curso>/', TCCCursoList.as_view(), name='listar_tcc_curso'),
    path('detalhar/tcc/<int:pk>/', TCCDetail.as_view(), name='detalhar_tcc_publicado'),
    path('criar/tcc/', TCCCreate.as_view(), name='criar_tcc'),
    path('editar/tcc/<int:pk>/', TCCUpdate.as_view(), name='editar_tcc'),
    path('deletar/tcc/<int:pk>/', TCCDelete.as_view(), name='deletar_tcc'),

    path('criar/autor/', AutorCreate.as_view(), name='criar_autor'),
    path('editar/autor/<int:pk>/', AutorUpdate.as_view(), name='editar_autor'),
    path('deletar/autor/<int:pk>/', AutorDelete.as_view(), name='deletar_autor'),
    path('listar/autores/', AutorList.as_view(), name='listar_autores'),

    path('criar/curso/', CursoCreate.as_view(), name='criar_curso'),
    path('editar/curso/<int:pk>/', CursoUpdate.as_view(), name='editar_curso'),
    path('deletar/curso/<int:pk>/', CursoDelete.as_view(), name='deletar_curso'),
    path('listar/curso/', CursoList.as_view(), name='listar_curso'),

    path('criar/orientador/', OrientadorCreate.as_view(), name='criar_orientador'),
    path('editar/orientador/<int:pk>/', OrientadorUpdate.as_view(), name='editar_orientador'),
    path('deletar/orientador/<int:pk>/', OrientadorDelete.as_view(), name='deletar_orientador'),
    path('listar/orientador/', OrientadorList.as_view(), name='listar_orientador'),
]
