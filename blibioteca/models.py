from django.db import models
from django.conf import settings
from datetime import date

class Livros(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=100, null=True, blank=False)
    capa = models.ImageField(upload_to='capa')
    autor = models.CharField(max_length=100, null=True, blank=True)
    co_autor = models.CharField(max_length=100, null=True, blank=True)
    data_cadastro = models.DateField(default=date.today, null=True, blank=True)
    emprestado = models.BooleanField(default=False)
    data_emprestimo = models.DateField(null=True, blank=True, default=date.today)
    data_devolucao = models.DateField(null=True, blank=True)
    emprestimo_duracao = models.DurationField(null=True, blank=True)
    
    class Meta:
        ordering = ['-data_cadastro']
        verbose_name_plural = 'Livros'
        
    def __str__(self) -> str:
        return f'Livro : {self.titulo} - Autor : {self.autor}'