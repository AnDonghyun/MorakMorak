from django.shortcuts import render
from .models import StartRelayNovel,RadioStation

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

