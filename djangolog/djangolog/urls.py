from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from enroll import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    url('log/', views.upload_csv, name='upload_csv'),
    url('success/', views.success, name='success'),
    url('error/', views.error, name='error'),
]

