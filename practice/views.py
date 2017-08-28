from django.shortcuts import render

# Create your views here.


def contents_list(request):
    response = render(request, 'practice/contents_list.html')
    return response