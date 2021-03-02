
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from file import views as fi
from enroll import views as en
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', en.add_show, name="addandshow"),
    path('delete/<int:id>/', en.delete_data, name="deletedata"),
    path('<int:id>/', en.update_data, name="updatedata"),
    url('upload/', fi.upload, name='upload'),
    url('success/', fi.success, name='success'),
    url('error/', fi.error, name='error'),
]

