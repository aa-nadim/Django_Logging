from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from firstAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('addUser/',views.addUser,name='addUser'),
    url('addSomething/',views.addSomething,name='addUser'),
    path('addNew/',views.addNew,name='addNew'),
    path('addNewError/',views.addNewError,name='addNewError'),
]
