from django.urls import re_path
from .import views


urlpatterns = [
    re_path(r'^$', views.devindex, name='devindex'),
    re_path(r'^devdashboard$', views.devdashboard, name='devdashboard'),
    re_path(r'^devReportedissues$', views.devReportedissues, name='devReportedissues'),
    re_path(r'^devreportissue$', views.devreportissue, name='devreportissue'),
    re_path(r'^devreportedissue$', views.devreportedissue, name='devreportedissue'),
    re_path(r'^devsuccess$', views.devsuccess, name='devsuccess'),
    re_path(r'^devissues$', views.devissues, name='devissues'),
     re_path(r'^manager_index', views.manager_index, name='manager_index'),
      re_path(r'^manager_projects', views.manager_projects, name='manager_projects'),
    
]