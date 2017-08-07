# practice/urls.py

from django.conf.urls import url
from . import views


urlpatterns = [ 
    url(r'^$', views.contents_list, name="contents_list"),

]   