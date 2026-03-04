from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Cliente
from .forms import FormularioCliente


class VistaListaClientes(ListView):
    model = Cliente
    template_name = 'clientes/lista.html'
    context_object_name = 'clientes'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        """Adiciona dados adicionais ao contexto."""
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Listar Clientes'
        return contexto


class VistaCriarCliente(CreateView):
    model = Cliente
    form_class = FormularioCliente
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('lista')
    
    def get_context_data(self, **kwargs):
        """Adiciona dados adicionais ao contexto."""
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Novo Cliente'
        contexto['botao'] = 'Cadastrar'
        return contexto
    
    def form_valid(self, formulario):
        """Processa validação do formulário."""
        resposta = super().form_valid(formulario)
        mensagem = f'✅ Cliente {self.object.nome} cadastrado com sucesso!'
        messages.success(self.request, mensagem)
        return resposta


class VistaEditarCliente(UpdateView):
    model = Cliente
    form_class = FormularioCliente
    template_name = 'clientes/form.html'
    success_url = reverse_lazy('lista')
    
    def get_context_data(self, **kwargs):
        """Adiciona dados adicionais ao contexto."""
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = f'Editar Cliente: {self.object.nome}'
        contexto['botao'] = 'Atualizar'
        return contexto
    
    def form_valid(self, formulario):
        """Processa validação do formulário."""
        resposta = super().form_valid(formulario)
        mensagem = f'✅ Cliente {self.object.nome} atualizado com sucesso!'
        messages.success(self.request, mensagem)
        return resposta


class VistaDeletarCliente(DeleteView):
    """Visualização para deletar cliente com confirmação.
    
    Attributes:
        model: Modelo Cliente
        template_name: Template de confirmação
        success_url: URL para redirecionamento após sucesso
    """
    model = Cliente
    template_name = 'clientes/confirmar_delecao.html'
    success_url = reverse_lazy('lista')
    
    def get_context_data(self, **kwargs):
        """Adiciona dados adicionais ao contexto."""
        contexto = super().get_context_data(**kwargs)
        contexto['titulo'] = 'Confirmar Deleção'
        return contexto
    
    def delete(self, requisicao, *args, **kwargs):
        """Executa deleção e exibe mensagem de sucesso."""
        cliente = self.get_object()
        resposta = super().delete(requisicao, *args, **kwargs)
        mensagem = f'✅ Cliente {cliente.nome} removido com sucesso!'
        messages.success(requisicao, mensagem)
        return resposta
