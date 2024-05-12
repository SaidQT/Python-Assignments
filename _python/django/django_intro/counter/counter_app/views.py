from django.shortcuts import render,redirect
def index(request):
    if not 'visits' in request.session:
        request.session['visits']=0
    if not 'counter' in request.session:
        request.session['counter']=0
    request.session['counter']+=1
    request.session['visits']+=1
    return render(request,"index.html")
def clear(request):
    del request.session['visits']
    del request.session['counter']
    return redirect("/")
def double(request):
    request.session['visits']+=1
    return redirect('/')
def add (request):
    request.session['visits']+=int(request.POST['quantity'])-1
    return redirect('/')
