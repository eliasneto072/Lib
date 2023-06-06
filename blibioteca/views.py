from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required

from rest_framework.decorators import api_view

from .models import Livros
from .serializers import *
from .forms import LivroForm


@api_view(['GET'])
def homeView(request):
    livros = Livros.objects.all()
    context={'livros':livros}
    return render(request, 'base.html', context)

from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

@login_required
@api_view(['GET'])
def listlivro(request):
    livros = Livros.objects.order_by('titulo')
    context={'livros':livros}
    return render(request, 'livros.html', context)

@login_required
@api_view(['POST', 'GET'])
def createlivro(request):
    if request.method == 'GET':
        forms = LivroForm()
    if request.method == 'POST':
        forms = LivroForm(request.POST, request.FILES)
        if forms.is_valid():
            livro = forms.save(commit=False)
            livro.usuario = request.user
            livro.capa = request.FILES['capa']
            livro.save()
            return redirect('livros')
    else:
        forms = LivroForm(initial={'usuario': request.user})
    
    context = {'forms': forms}
    return render(request, 'create.html', context)

