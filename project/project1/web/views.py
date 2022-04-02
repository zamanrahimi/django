from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# from project.project1.web.models import Destination
# Create your views here.



def index(request):
    des1 = Destination()
    des1.name='Hello from destination one'
    des1.fname='Ali'
    des1.img='banner.jpg'
    des1.bon=True
    


    des2 = Destination()
    des2.name='Hello from destination two'
    des2.fname='Karim'
    des2.img='logo.png'
    des2.bon=True
    
    dests = [des1, des2]

    return render(request, 'index.html', {'dests': dests})


