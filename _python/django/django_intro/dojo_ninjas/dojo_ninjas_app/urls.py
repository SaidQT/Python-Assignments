from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('process', views.post),
    path('process2',views.post2),
]