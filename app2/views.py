from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
        return HttpResponse("<h1> Hola Mundo </h1>")

def pagina2(request):
    html="""
            <p>Esta es mi segunda APP (app2).</p>
            <h2>Soy un subtitulo de app2</h2>
"""
    return HttpResponse(html)