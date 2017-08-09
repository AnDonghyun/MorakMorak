# hub/views.py
from django.shortcuts import render
from .models import MyNovel

# Create your views here.
def mynovel(request):
    my_novel = MyNovel.objects.all()
    return render(request, 'hub/mynovel.html')


def sharednovel(request):
    shared_novel = MyNovel.objects.all()
    return render(request, 'hub/sharednovel.html',{
        'sharednovel': shared_novel
        })
