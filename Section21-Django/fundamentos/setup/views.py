from django.shortcuts import render

def homepage(request):
    nome = "Fulano"
    pessoa = {
        'nome': 'Maria Da Silva',
        'idade': 30,
        'cidade': 'São Paulo'
    }
    return render(request, 'home.html', {'nome':nome, 'pessoa':pessoa})

def about(request):
    frutas = ['Maçã', 'Banana', 'Laranja', 'Uva']
    return render(request, 'about.html', {'frutas':frutas})