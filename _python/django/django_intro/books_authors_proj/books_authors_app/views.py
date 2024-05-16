from django.shortcuts import render,redirect
from . models import Book,Author

def index(request):
    context={
        "books":Book.objects.all(),
    }
    return render(request,'index.html',context)

def add(request):
    if request.method=="POST":
        title=request.POST['Title']
        description=request.POST['desc']
    create= Book.objects.create(title=title,desc=description)
    return redirect('/')

def show_book(request,id):
    book_x=Book.objects.get(id=id)
    data={
        "book_title":book_x.title,
        "book_desc":book_x.desc,
        "book_authors":book_x.authors.all(),
        "book_id":book_x.id,
        "authors":Author.objects.all(),
    }
    return render(request,"book.html", data)

def add_author(request,id):
    book_y=Book.objects.get(id=id)
    if request.method=='POST':
        author=request.POST['authors']
    author_y=Author.objects.get(id=author)
    book_y.authors.add(author_y)
    return redirect(f'/books/{id}')
    
def authors(request):
    context2={
        "authors":Author.objects.all(),
    }
    return render(request,'author.html',context2)

def create_author(request):
    if request.method=='POST':
        firstname=request.POST['f-name']
        lastname=request.POST['l-name']
        notes=request.POST['desc']
    Author.objects.create(first_name=firstname,last_name=lastname,notes=notes)
    return redirect("/authors")
    
def show_author(request,z):
    author_x=Author.objects.get(id=z)
    data2={
        "id":author_x.id,
        "first name":author_x.first_name,
        "last name":author_x.last_name,
        "notes":author_x.notes,
        "books":Book.objects.all(),
        "author_books":Author.books.all(),
    }
    return render(request,"showauthor.html",data2)