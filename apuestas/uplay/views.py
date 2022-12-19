import requests
from django.shortcuts import render

# Create your views here.
def home(request):
    response=requests.get('http://127.0.0.1:8000/usuarios').json()
    print(response)
    return render(request, 'Home.html', {'data': response})

def apuestas(request):
    response=requests.get('http://127.0.0.1:8000/usuarios').json()
    print(response)
    return render(request, 'Apuestas.html', {'data': response})
    
def resultados(request):
    response=requests.get('http://127.0.0.1:8000/usuarios').json()
    response = sorted(response, key=lambda d: d['puntos'], reverse=True) 
    n = 1
    for i in response:
        i['index'] = n
        n = n+1
    print(response)
    return render(request, 'Resultados.html', {'data': response})
