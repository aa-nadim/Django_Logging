from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('addUser/', views.addUser, name='addUser'),
    url('addSomething/', views.addSomething, name='addUser'),
    path('addNew/<someNumber>', views.addNew, name='addNew'),
    path('addNewError/<someNumber>', views.addNewError, name='addNewError'),
]