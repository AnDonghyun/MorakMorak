# hub/urls.py

from django.conf.urls import url
from . import views


urlpatterns = [ 
    url(r'^$', views.list, name='hub_list'),
    url(r'^mynovel/$', views.mynovel, name='my_novel'),
    url(r'^sharednovel/$', views.sharednovel, name='shared_novel'),
    url(r'^mynovel/(?P<id>\d+)/$', views.post_detail, name='post_detail'),		
    url(r'^mynovel/new/$', views.post_new, name='post_new'),		
    url(r'^mynovel/(?P<id>\d+)/edit/$', views.post_edit, name = 'post_edit'),
    
]   
