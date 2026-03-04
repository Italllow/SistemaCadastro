from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
    # Colunas exibidas na lista de clientes
    list_display = ('id', 'nome', 'email', 'telefone', 'data_criacao')
    
    # Filtros laterais disponíveis
    list_filter = ('data_criacao',)
    
    # Campos pesquisáveis
    search_fields = ('nome', 'email', 'telefone')
    
    # Ordenação padrão
    ordering = ('-data_criacao',)
    
    # Campos somente leitura
    readonly_fields = ('data_criacao',)
    
    # Agrupamento de campos na tela de edição
    fieldsets = (
        ('Informações Principais', {
            'fields': ('nome', 'email', 'telefone'),
            'description': 'Dados principais do cliente'
        }),
        ('Registro', {
            'fields': ('data_criacao',),
            'classes': ('collapse',),
            'description': 'Informações de registro'
        }),
    )

    def save_model(self, requisicao, objeto, formulario, mudou):
        super().save_model(requisicao, objeto, formulario, mudou)

    def delete_model(self, requisicao, objeto):
        super().delete_model(requisicao, objeto)
