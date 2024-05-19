from django.shortcuts import render,redirect
from .models import Show
from django.contrib import messages

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
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('shows/new')
    else:
        if request.method=="POST":
            title=request.POST['title']
            network=request.POST['network']
            release_date=request.POST['release_date']
            desc=request.POST['desc']        
        obj_x=Show.objects.create(title=title,network=network,release_date=release_date,desc=desc)
        messages.success(request, "Show successfully added")
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
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
        edit_show=Show.objects.get(id=id)
        edit_show.title=request.POST['title']
        edit_show.network=request.POST['network']
        edit_show.desc=request.POST['desc']
        edit_show.release_date=request.POST['release_date']
        edit_show.save()
        messages.success(request, "Show successfully updated")
        return redirect('/')