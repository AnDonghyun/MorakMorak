# hub/urls.py

from django.conf.urls import url
from . import views


urlpatterns = [ 
    # url(r'^$', views.list, name='list'),
    url(r'^mynovel^$', views.mynovel, name='my_novel'),
    url(r'^sharednovel^$', views.sharednovel, name='shared_novel'),

]   
