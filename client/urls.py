from django.contrib import admin
from django.urls import re_path,include
from app import views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('app.urls')),
    re_path(r'^$', views.devindex, name='devindex'),
]