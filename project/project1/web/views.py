from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
# from project.project1.web.models import Destination
# Create your views here.



def index(request):
    dests = Destination.objects.all()

    return render(request, 'index.html', {'dests': dests})


