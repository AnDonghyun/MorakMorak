# hub/views.py
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from .models import MyNovel
from django.http import Http404
from .forms import PostForm

# Create your views here.
def mynovel(request):
    my_novel = MyNovel.objects.all() 
    print(request.user)#접속한 사용자의 아이디를 알 수 있음 

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

def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(MyNovel,id=id)
    return render(request, 'hub/post_detail.html',{
            'post':post,
        })

def post_edit(request, id):
    post = get_object_or_404(MyNovel, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) 
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수정하였습니다.')
            return redirect(post) #post.get_absolute_url() => post detail
    else:
        form = PostForm(instance=post)
    return render(request, 'hub/post_form.html', {
            'form':form,
        })


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, '새 포스팅을 저장하였습니다.')
            return redirect(post) #post.get_absolute_url() => post detail
    else:
        form = PostForm()
    return render(request, 'hub/post_form.html', {
            'form':form,
        })
