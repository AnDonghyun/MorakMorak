"""morakmorak URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from django.shortcuts import redirect


#def root(request):
#    return redirect('첫화면으로 지정할 html file')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')), #장고 기본 auth앱과 연동해서 사용하므로, namespace 적용하지 않음! 
    url(r'^accounts/', include('allauth.urls')), #include를 사용할 시에는 url에 $를 표시하면 안됨. $ 표시할 경우 패턴매칭 끝남.
    url(r'^hub/', include('hub.urls', namespace='hub')),
    url(r'^practice/', include('practice.urls', namespace='practice')),
   
]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
   ]
#runserver 실행했을때, debug toolbar 활성화