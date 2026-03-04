from django.urls import path
from . import views

# Padrão de URLs para operações CRUD
urlpatterns = [
    # GET /clientes/ - Lista todos os clientes
    path('', views.VistaListaClientes.as_view(), name='lista'),
    
    # GET /clientes/novo/ - Formulário para novo cliente
    # POST /clientes/novo/ - Cria novo cliente
    path('novo/', views.VistaCriarCliente.as_view(), name='criar'),
    
    # GET /clientes/<id>/editar/ - Formulário para editar cliente
    # POST /clientes/<id>/editar/ - Atualiza cliente
    path('<int:pk>/editar/', views.VistaEditarCliente.as_view(), name='editar'),
    
    # GET /clientes/<id>/deletar/ - Confirmação de deleção
    # POST /clientes/<id>/deletar/ - Deleta cliente
    path('<int:pk>/deletar/', views.VistaDeletarCliente.as_view(), name='deletar'),
]
