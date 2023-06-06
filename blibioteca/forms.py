from django import forms
from .models import Livros

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livros
        fields = ['titulo', 'autor', 'co_autor', 'emprestado', 'data_emprestimo', 'data_devolucao', 'capa' ,]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['usuario'].widget = forms.HiddenInput