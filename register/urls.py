from xml.etree.ElementInclude import include
from django.urls import path

from . import views

app_name = 'register'
urlpatterns = [
    path('', views.user_form, name='user_insert'),
    path('<int:id>', views.user_form, name='user_update'),
    path('delete/<int:id>', views.user_delete, name='user_delete'),
    path('list/', views.user_list, name='user_list'),
]
