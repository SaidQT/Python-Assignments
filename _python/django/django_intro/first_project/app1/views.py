from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def root(request):
    return redirect('/blogs')

def new (request):
    return HttpResponse("placeholder to display a new form to create a new blog" )

def create(request):
    return redirect('/')

def show(request,number):
    return HttpResponse(f"A placeholder to display blog number: {number}")

def edit(request,number):
    return HttpResponse(f"A placeholder to edit blog {number}")

def destroy (request,number):
    return redirect('/blogs')

def hello(request): 
    dict=  {
    "title":"My first blog",
    "content":"lorem, ipsum as sawqe pas sa wq we q",
}
    return JsonResponse(dict)