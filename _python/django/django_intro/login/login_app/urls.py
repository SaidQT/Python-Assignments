from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('process',views.create),
    path('success',views.success),
    path('process2',views.login),
    path('delete',views.delete)
]