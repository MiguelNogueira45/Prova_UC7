from django.shortcuts import render
from .forms import FilmesForm
from django.http import HttpRequest
from .models import Lista_FilmesModel
from django.shortcuts import render, get_object_or_404, redirect
from .models import Lista_FilmesModel



# Create your views here.
def filmes_principal(request:HttpRequest):
    if request.method == "POST":
        formulario = FilmesForm(request.POST)
        if formulario.is_valid():
            formulario.save()
    contexto = {

        'filmes': Lista_FilmesModel.objects.all(),
        'form': FilmesForm
    }


    return render(request, 'filmes.html', contexto)


def excluir_filme(request, id):
    filme = get_object_or_404(Lista_FilmesModel, id=id)

    if request.method == 'POST':
        filme.delete()
        return redirect('filmes:principal_filmes')  # Troca por onde você lista os filmes

    return render(request, 'excluir_filme.html', {'filme': filme})
