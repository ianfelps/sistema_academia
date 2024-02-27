from django.shortcuts import render
from .models import Cliente

# Create your views here.
def cad(request):
    return render(request, 'paginas/cad.html')

def list(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        plano = request.POST.get('plano')
        adesao = request.POST.get('adesao')

        if nome and cpf and email and plano and adesao:
            novo_cliente = Cliente()
            novo_cliente.nome = nome
            novo_cliente.cpf = cpf
            novo_cliente.email = email
            novo_cliente.plano = plano
            novo_cliente.adesao = adesao
            novo_cliente.save()

    clientes = Cliente.objects.all()
    return render(request, 'paginas/list.html', {'list': clientes})
