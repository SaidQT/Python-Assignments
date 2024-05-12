from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def result(request):
    selected_languages = request.POST.getlist('speak')
    context= {
        "name":request.POST['x'],
        "location":request.POST['location'],
        "language":request.POST['language'],
        "message":request.POST['message'],
        "gender":request.POST['gender'],
        "speak":selected_languages
    }
    
    return render(request,'show.html',context)
