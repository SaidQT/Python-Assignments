from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('process',views.create),
    path('wall',views.success),
    path('process2',views.login),
    path('delete',views.delete),
    path('message/<int:id>',views.message),
    path('comment/<int:z>/<int:y>', views.comment),
    path('delete/<int:x>', views.delete_comment),
]