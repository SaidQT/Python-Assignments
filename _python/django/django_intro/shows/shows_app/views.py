from django.shortcuts import render,redirect
from .models import Show
def red(request):
    return redirect('/shows/')
def index(request):
    context={
        "shows":Show.objects.all(),
    }
    return render(request,"index.html",context)

def new(request):
    return render(request,"new.html")

def add(request):
    if request.method=="POST":
        title=request.POST['title']
        network=request.POST['network']
        release_date=request.POST['release_date']
        desc=request.POST['desc']        
    obj_x=Show.objects.create(title=title,network=network,release_date=release_date,desc=desc)
    return redirect(f"shows/{obj_x.id}")

def delete(request,id):
    show=Show.objects.get(id=id)
    show.delete()
    return redirect('/shows/')


def show(request,id):
    data={
        "show":Show.objects.get(id=id)
    }
    return render(request,"show.html", data)

def edit(request,id):
    data={
        "show":Show.objects.get(id=id)
    }
    return render(request,'edit.html',data)

def update(request,id):
    edit_show=Show.objects.get(id=id)
    edit_show.title=request.POST['title']
    edit_show.network=request.POST['network']
    edit_show.desc=request.POST['desc']
    edit_show.release_date=request.POST['release_date']
    edit_show.save()
    return redirect('/')