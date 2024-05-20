from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
import bcrypt

def index(request):
    return render(request,'index.html')


def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value,extra_tags="fail")
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        print (pw_hash)
        if request.method == "POST":
            user=User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=pw_hash
                )
            request.session['userid'] = user.id
    return redirect('/success')

def login(request):
    email = User.objects.filter(email=request.POST['email']) 
    if email: 
        logged_email = email[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_email.password.encode()):
            request.session['userid'] = logged_email.id
            return redirect('/success')
    messages.error(request, "The password or email you entered is incorrect",extra_tags="login")
    return redirect("/")

def success(request):
    if "userid" not in request.session:
        return redirect("/")
    data={"user":User.objects.get(id=request.session['userid']),
                "messages":Message.objects.all(),
                "comments":Comment.objects.all(),
}
    return render(request,'success.html',data)

def delete(request):
    request.session.clear()
    return redirect('/')

def message(request,id):
    user_1=User.objects.get(id=id)
    Message.objects.create(users=user_1,
                    message=request.POST['message'])
    return redirect('/success')


def comment(request,z,y):
    msg_x=Message.objects.get(id=y)
    user_x=User.objects.get(id=z)
    Comment.objects.create(users=user_x,messages=msg_x,comment=request.POST['comment'])
    return redirect('/success')

def delete_comment(request,x):
    comment_x=Comment.objects.get(id=x)
    comment_x.delete()
    return redirect('/success')
    
