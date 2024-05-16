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
        "not_author":Author.objects.exclude(books=book_x),
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
        "author_id":author_x.id,
        "first_name":author_x.first_name,
        "last_name":author_x.last_name,
        "notes":author_x.notes,
        "author_books":author_x.books.all(),
        "books":Book.objects.all(),
        "not_books":Book.objects.exclude(authors=author_x)
    }
    return render(request,"showauthor.html",data2)

def add_book(request,z):
    author_y=Author.objects.get(id=z)
    if request.method=='POST':
        y=request.POST['books']
    book_y=Book.objects.get(id=y)
    author_y.books.add(book_y)
    return redirect(f'/authors/{z}')
    
