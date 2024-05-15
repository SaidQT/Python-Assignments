from django.shortcuts import render,redirect
from . models import Dojo,Ninja
def index(request):
    data={
        "dojos": Dojo.objects.all(),
    }
    return render(request, "index.html",data)

def post(request):
    first=request.POST['fname']
    city=request.POST['city']
    state=request.POST['state']
    Dojo.objects.create(name=first,city=city,state=state)
    return redirect('/')

def post2(request):
    name=request.POST['firstname']
    lname=request.POST['lastname']
    x = request.POST['dojo']
    dojo = Dojo.objects.get(name=x)
    Ninja.objects.create(dojo_id=dojo,first_name=name,last_name=lname)
    
    return redirect('/')
