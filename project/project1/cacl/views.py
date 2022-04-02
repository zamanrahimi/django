from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html', {
        'name': 'ali'
    })

def add(request): 
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result': res})
