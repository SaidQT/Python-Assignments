from django.shortcuts import render
from time import gmtime, strftime
from datetime import datetime    

def index(request):
    local_time=datetime.now()
    context = {
        "time": strftime("  %H:%M:%S %p %d-%m-%Y", gmtime()),
        "localtime":local_time
    }
    return render(request,'index.html', context)

