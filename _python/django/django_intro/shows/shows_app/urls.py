from django.urls import path
from . import views	

urlpatterns = [
    path('',views.red),
    path('shows/', views.index),
    path('shows/new', views.new),
    path('process',views.add),
    path('shows/<int:id>/destroy', views.delete),
    path('shows/<int:id>', views.show),
    path('shows/<int:id>/edit', views.edit),
    path('update/<int:id>', views.update)
]