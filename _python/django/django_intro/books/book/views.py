from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User,Book
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
    return redirect('/books')

def login(request):
    email = User.objects.filter(email=request.POST['email']) 
    if email: 
        logged_email = email[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_email.password.encode()):
            request.session['userid'] = logged_email.id
            return redirect('/books')
    messages.error(request, "The password or email you entered is incorrect",extra_tags="login")
    return redirect("/")


def show(request):
    if "userid" not in request.session:
        return redirect("/")
    data={
        "user":User.objects.get(id=request.session['userid']),
        "books":Book.objects.all(),
    }
    return render(request,'book.html',data)

def add(request):
    user=User.objects.get(id=request.session['userid'])
    if request.method == "POST":
        errors = Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        Book.objects.create(title=request.POST['title'], desc=request.POST['desc'], uploaded_by=user)
        book=Book.objects.get(title=request.POST['title'])
        book.favorites.add(user)
        return redirect("/books")

def add_to_favorites(request,x,y):
    book_x=Book.objects.get(id=x)
    user_x=User.objects.get(id=y)
    book_x.favorites.add(user_x)
    return redirect('/books')

def remove_favorite2(request,x,y):
    book_x=Book.objects.get(id=x)
    user_x=User.objects.get(id=y)
    book_x.favorites.remove(user_x)
    return redirect(f'/books/{x}')

def add_to_favorites2(request,x,y):
    book_x=Book.objects.get(id=x)
    user_x=User.objects.get(id=y)
    book_x.favorites.add(user_x)
    return redirect(f'/show/{x}')
    

def show_book(request,id):
    data={
        "user":User.objects.get(id=request.session['userid']),
        "book_y":Book.objects.get(id=id)
    }
    return render(request,'show.html',data)
    
def edit_book(request,id):
    book_y=Book.objects.get(id=id)
    if request.method == "POST":
        book_y.title=request.POST['name']
        book_y.desc=request.POST['description']
        book_y.uploaded_by=User.objects.get(id=request.session['userid'])
        book_y.save()
    return redirect(f'/books/{id}')

def remove_book(request,m):
    book_y=Book.objects.get(id=m)
    book_y.delete()
    return redirect(f'/books/{m}')
    
def show_book2(request,id):
    data={
        "user":User.objects.get(id=request.session['userid']),
        "book_y":Book.objects.get(id=id),
        "books":Book.objects.all(),
    }
    return render(request,'show2.html', data)
    
def delete(request):
    request.session.clear()
    return redirect('/')

def remove_favorite(request,x,y):
    book_x=Book.objects.get(id=x)
    user_x=User.objects.get(id=y)
    book_x.favorites.remove(user_x)
    return redirect(f'/show/{x}')
    

    

