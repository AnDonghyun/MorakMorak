from django.shortcuts import get_object_or_404, render, redirect
from .models import StartRelayNovel,RadioStation
from .forms import PostForm
from django.contrib import messages
from django.http import Http404


# Create your views here.


def contents_list(request):  
    response = render(request, 'practice/contents_list.html')
    return response


def relaynovel(request):
    relaynovel = StartRelayNovel.objects.all()
    return render(request, 'practice/relaynovel_list.html', {
        'relaynovel_list': relaynovel,
        })


def radiostation(request):
    radiostation = RadioStation.objects.all()
    return render(request, 'practice/radiostation.html', {
        'radiostation_list': radiostation,
        })


def post_detail(request, id):
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(StartRelayNovel,id=id)
    return render(request, 'practice/post_detail.html',{
            'post':post,
        })

def post_edit(request, id):
    post = get_object_or_404(StartRelayNovel, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post) 
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수정하였습니다.')
            return redirect(post) #post.get_absolute_url() => post detail
    else:
        form = PostForm(instance=post)
    return render(request, 'practice/post_form.html', {
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
    return render(request, 'practice/post_form.html', {
            'form':form,
        })
