from django.db import models


class Cliente(models.Model):
    nome = models.CharField(
        max_length=100,
        verbose_name="Nome",
        help_text="Digite o nome completo do cliente"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="E-mail válido e único para contato"
    )
    telefone = models.CharField(
        max_length=20,
        verbose_name="Telefone",
        help_text="Número de telefone para contato"
    )
    data_criacao = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Data de Criação",
        help_text="Data e hora de criação do registro"
    )

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-data_criacao']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['-data_criacao']),
        ]

    def __str__(self):
        """Retorna representação em string do cliente."""
        return f"{self.nome} - {self.email}"
