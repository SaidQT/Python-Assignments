from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('process',views.create),
    path('process2',views.login),
    path('delete',views.delete),
    path('books',views.show),
    path('add',views.add),
    path('add/<int:x>/<int:y>',views.add_to_favorites),
    path('edit/<int:id>',views.edit_book),
    path('adding/<int:x>/<int:y>',views.add_to_favorites2),
    path('books/<int:id>', views.show_book),
    path('show/<int:id>', views.show_book2),
    path('remove/<int:x>/<int:y>',views.remove_favorite),
    path('del/<int:m>',views.remove_book),
    path('unfav/<int:x>/<int:y>', views.remove_favorite2)
]