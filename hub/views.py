# hub/views.py
from django.shortcuts import render
from .models import MyNovel

# Create your views here.
def mynovel(request):
    my_novel = MyNovel.objects.all()
    return render(request, 'hub/mynovel.html', {
        'novel_list': my_novel,
        })


def sharednovel(request):
    shared_novel = MyNovel.objects.all()
    return render(request, 'hub/sharednovel.html',{
        'novel_list': shared_novel,
        })


def list(request):
    return render(request, 'hub/hublist.html')
