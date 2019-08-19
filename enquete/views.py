from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Pergunta

# Create your views here.
def index(request):
	ultimas_perguntas = Pergunta.objects.order_by('-data_pub')[:5]
	contexto = {'ultimas_perguntas': ultimas_perguntas}
	return render(request, 'enquete/index.html', contexto)

def detalhes(request, id_pergunta):
	pergunta = get_object_or_404(Pergunta, pk=id_pergunta)
	return render(request, 'enquete/detalhes.html', {'pergunta':pergunta})

def resultados(request, id_pergunta):
	resposta = "Apresentação dos resultados da pergunta %s."
	return HttpResponse(resposta % id_pergunta)

def votacao(request, id_pergunta):
	resposta = "Votação para a questão %s."
	return HttpResponse(resposta % id_pergunta)