from django import forms
from .models import Cliente


class FormularioCliente(forms.ModelForm):
    email = forms.EmailField(
        label="Endereço de E-mail",
        help_text="Digite um e-mail válido",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'seu@email.com',
            'aria-label': 'Endereço de E-mail'
        })
    )
    
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone']
        labels = {
            'nome': 'Nome Completo',
            'email': 'Endereço de E-mail',
            'telefone': 'Telefone',
        }
        help_texts = {
            'nome': 'Digite o nome completo do cliente',
            'email': 'Um e-mail válido e único',
            'telefone': 'Número com DDD para contato',
        }
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'João Silva',
                'aria-label': 'Nome Completo',
            }),
            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(11) 99999-9999',
                'aria-label': 'Telefone',
            }),
        }

    def limpar_email(self):
        email = self.cleaned_data.get('email')
        if email:
            if Cliente.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise forms.ValidationError("Este e-mail já está cadastrado no sistema.")
        return email

    def limpar_telefone(self):
        telefone = self.cleaned_data.get('telefone')
        if telefone and len(telefone.replace(' ', '').replace('-', '')) < 10:
            raise forms.ValidationError("Telefone deve ter pelo menos 10 dígitos.")
        return telefone
