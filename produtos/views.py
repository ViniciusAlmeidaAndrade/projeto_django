from django.shortcuts import render
from django.http import HttpResponse

def relatorio_vist(request):
    if request.method == "GET":
        nome="caio"
        return render(request, 'relatorio_vist.html')
    elif request.method == "POST":
        n_tecnico= request.POST.get("n_tecnico")
        n_cliente=request.Post.get("n_cliente")
        print(n_tecnico)
        return HttpResponse("Estou no inserir")
def inserir_produto(request):
    return HttpResponse('Estou no inserir')
