from django.shortcuts import render, redirect
from app.models import Agenda

# Create your views here.
def index(request):
    contatos = Agenda.listar()
    return render(request, 'index.html', {'contatos': contatos})

def novo_contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        print(nome, telefone)
        Agenda.novo(nome, telefone)
        return redirect('index')
    return render(request, 'index.html')

def deletar_contato(request, id):
    Agenda.deletar(id)
    return redirect('index')