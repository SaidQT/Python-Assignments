from django.shortcuts import render,redirect
import random
from time import localtime, strftime
    
def index(request):
    if 'gold' not in request.session:
        request.session['gold']=0
    return render(request,"index.html")
def play(request):
    if 'results' not in request.session:
        request.session['results']=[]
    if request.method=="POST":
        if request.POST['game'] == 'cave':
            request.session['random_num']=random.randint(10,20)
            request.session['results'].append(f"You entered a cave and earned {request.session['random_num']}. {strftime("%Y-%m-%d %H:%M %p", localtime())}")
        if request.POST['game'] == 'house':
            request.session['random_num']=random.randint(10,20)
            request.session['results'].append(f"You entered a house and earned {request.session['random_num']}. {strftime("%Y-%m-%d %H:%M %p", localtime())}")
        if request.POST['game']== 'farm':
            request.session['random_num']=random.randint(10,20)
            request.session['results'].append(f"You entered a farm and earned {request.session['random_num']}. {strftime("%Y-%m-%d %H:%M %p", localtime())}")
        if request.POST['game']=='quest':
            request.session['random_num']=random.randint(-50,50)
            if request.session['random_num'] >0:
                request.session['results'].append(f"You completed a quest and earned {request.session['random_num']}. {strftime("%Y-%m-%d %H:%M %p", localtime())}")
            if request.session['random_num'] < 0:
                request.session['results'].append(f"You failed a quest and lost {abs(request.session['random_num'])}. {strftime("%Y-%m-%d %H:%M %p", localtime())}")
        request.session['gold']+=request.session['random_num']
    return redirect('/')
    
def reset(request):
    del request.session['gold']
    del request.session['results']
    return redirect('/')
    