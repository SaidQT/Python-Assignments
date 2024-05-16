from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    path('process',views.add),
    path('books/<int:id>', views.show_book),
    path('process2/<int:id>', views.add_author),
    path('authors', views.authors),
    path('process3',views.create_author),
    path('authors/<int:z>', views.show_author),
    ]