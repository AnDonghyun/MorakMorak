# practice/urls.py

from django.conf.urls import url
from . import views


urlpatterns = [ 
    url(r'^$', views.contents_list, name="contents_list"),
    url(r'^relaynovel/$', views.relaynovel, name="relay_novel"),
    url(r'^radiostation/$', views.radiostation, name="radio_station"),

]   