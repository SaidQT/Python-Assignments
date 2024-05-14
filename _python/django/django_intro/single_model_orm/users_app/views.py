from django.shortcuts import render,redirect
from .models import Users
def index(request):
    context={
        "users":Users.objects.all()
    }
    return render(request,"index.html",context)

def user(request):
    
    first= request.POST['first_name']
    last=request.POST['last_name']
    email=request.POST['Email']
    age=request.POST['age']

    create= Users.objects.create(first_name=first,last_name=last,email_address=email,age=age)
    return redirect('/')
    