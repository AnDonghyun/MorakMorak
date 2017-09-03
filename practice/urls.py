# practice/urls.py

from django.conf.urls import url
from . import views


urlpatterns = [ 
    url(r'^$', views.contents_list, name="contents_list"),
    url(r'^relaynovel/$', views.relaynovel, name="relay_novel"),
    url(r'^radiostation/$', views.radiostation, name="radio_station"),
    url(r'^relaynovel/(?P<id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^relaynovel/new/$', views.post_new, name='post_new'),
    url(r'^relaynovel/(?P<id>\d+)/edit/$', views.post_edit, name = 'post_edit'),
]   