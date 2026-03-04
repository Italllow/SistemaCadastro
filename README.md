# Sistema de Cadastro Django

Sistema web de gerenciamento de clientes construído com Django e Bootstrap 5.

## Inicialização Rápida

### 1. Instalar Dependências
```powershell
pip install django
```

### 2. Executar Servidor
```powershell
python manage.py runserver
```

### 3. Acessar a Aplicação
- **Web**: http://127.0.0.1:8000/clientes/
- **Admin**: http://127.0.0.1:8000/admin/


## Credenciais Admin

**Usuário**: `admin`

Para alterar a senha:
```powershell
python manage.py changepassword admin
```

## Funcionalidades

| Funcionalidade | URL | Método |
|---|---|---|
| Listar Clientes | `/clientes/` | GET |
| Novo Cliente | `/clientes/novo/` | GET/POST |
| Editar Cliente | `/clientes/<id>/editar/` | GET/POST |
| Deletar Cliente | `/clientes/<id>/deletar/` | GET/POST |
| Admin | `/admin/` | GET |


## Estrutura do Projeto

```
Sistema de Cadastro/
├── clientes/              # App principal
│   ├── migrations/        # Histórico de mudanças no BD
│   ├── templates/         # Templates HTML
│   ├── models.py          # Modelo de dados
│   ├── views.py           # Lógica das páginas
│   ├── forms.py           # Formulários
│   ├── urls.py            # Rotas
│   └── admin.py           # Interface admin
│
├── config/                # Configuração do Django
│   ├── settings.py        # Configurações
│   ├── urls.py            # URLs principais
│   └── wsgi.py            # WSGI
│
├── manage.py              # Gerenciador Django
├── db.sqlite3             # Banco de dados
└── README.md              # Este arquivo
```


## Comandos Úteis

### Criar migrações
```powershell
python manage.py makemigrations
```

### Aplicar migrações
```powershell
python manage.py migrate
```

### Criar superusuário
```powershell
python manage.py createsuperuser
```

### Acessar shell interativo
```powershell
python manage.py shell
```


## Configurações

- **Idioma**: Português (pt-br)
- **Timezone**: America/Sao_Paulo
- **Banco de Dados**: SQLite3
- **CSS Framework**: Bootstrap 5


## Campos do Cliente

- **Nome**: Campo de texto (até 100 caracteres)
- **Email**: Campo de e-mail único
- **Telefone**: Campo de telefone (até 20 caracteres)
- **Data de Criação**: Automático


## Validações

-  Email deve ser válido e único
-  Telefone deve ter mínimo 10 dígitos
-  Nome não pode estar vazio
-  Confirmação antes de deletar cliente


## Licença

Projeto educacional - Livre para uso e modificação.

---

**Última atualização**: 4 de março de 2026
