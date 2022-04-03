from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Emp
# from project.project1.web.models import Destination
# Create your views here.




# select information from database 
def index(request):
    dests = Emp.objects.all()

    return render(request, 'index.html', {'dests': dests})

# insert information into the database 
def insert(request):

    if request.method == "POST":
        name = request.POST['name']
        desc = request.POST['desc']
        emp = Emp.objects.create(name=name, desc=desc)
        emp.save()
        return redirect(index)
    else:
        pass 

    return render(request, 'index.html')
# delete information from the database
def delete_item(request, myid):
    Emp.objects.filter(id=myid).delete()
    return redirect(index)

# select the information in order to edit 
def update_item(request, myid):
    item_edit = Emp.objects.get(id=myid)
    dests = Emp.objects.all()
    context = {
        'item_edit': item_edit,
        'dests':dests 
    }
    return render(request, 'index.html', context )
  

# update the changed information 
def update_item1(request, myid):
    update1 = Emp.objects.get(id=myid)
    update1.name = request.POST['name']
    update1.desc = request.POST['desc']
    update1.save()
    return redirect(index)
  