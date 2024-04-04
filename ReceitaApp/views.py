from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

# Create your views here.
def listar_receitas(request):
    nome = 'dede'
    ingredientes = ['pão', 'manteiga']
    #dicionario de dados para template
    #chave : valor
    context = {
            'Endereco' : 'minha vida',
            'Bairro' : 'meu coração',
            'Cidade' : 'minha mente',
            'Estado' : 'apaixonado',
            'nome' : nome,
            'Ingredientes' : ingredientes
    }
    #qual tmplede essa view vai retorna
    return render (request, 'receitas.html', context)
