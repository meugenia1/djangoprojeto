
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.context import RequestContext
from django.template.loader import LoaderOrigin
from coded.models import Curso


# Create your views here.
def artigo(request,ano):
    return HttpResponse("ola mundo"+ano)

def home(request):
    cursosdest= Curso.objects.all().filter(Destaque="Destaque")
    cursos= Curso.objects.all()
    categoria= Curso.objects.all().filter(Categoria="??")  # @UnusedVariable
    template=LoaderOrigin('index.html')
    context= RequestContext(request,{'cursosdest':cursosdest}, {'cursos':cursos}, {"categoria":categoria})
    return HttpResponse(template.render(context))