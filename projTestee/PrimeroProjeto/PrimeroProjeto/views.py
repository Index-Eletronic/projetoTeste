from django.http import HttpResponse
from django.shortcuts import render

def hello(resquest):
    return render(resquest, 'index.html')

def articles(resquest, year):
    return HttpResponse ('O ano passado enviado foi: ' + str(year))

def lerDoBanco(nome):
    lista_nomes = [
        {'nome': 'Ana', 'idade': 20},
        {'nome': 'Pedro', 'idade': 25},
        {'nome': 'Joaquim', 'idade': 27}
    ]

    for pessoa in lista_nomes:
        if pessoa['nome'] == nome:
            return pessoa
    else:
        return {'nome': 'NÃO ENCONTADO', 'idade': 0}


def fnome(request, nome):
    result = lerDoBanco(nome)
    if result['idade'] > 0:
        return HttpResponse('A pessoa foi encontrada, ela tem: ' + str(result['idade']) + ' anos')
    else:
        return HttpResponse('Pessoa não encontrada')

def fname2(request, nome):
    idade = lerDoBanco(nome)['idade']
    return render(request, 'pessoa.html', {'v_idade': idade})