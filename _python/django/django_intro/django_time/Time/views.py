from django.shortcuts import render
from time import gmtime, strftime
from time import localtime, strftime
    
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime()),
        "localtime":strftime("%Y-%m-%d %H:%M %p" , localtime())
    }
    return render(request,'index.html', context)

