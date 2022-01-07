from django.shortcuts import render,redirect,HttpResponse

from channels.layers import get_channel_layer
import json
from .models import tutorial
from auapp.models import EventsModel  
import requests

def index(request):
    if request.user.is_authenticated:
        return render(request,'index.html')
    else:
        return redirect("user_login")
    

def hiit(request):
    Tut = tutorial.objects.all()
    context = {
	'Tut': Tut,
	}
    return  render(request, 'hiit.html', context)
    

def yoga(request):
    return render(request,"yoga.html")

def video(request,pk):
    Tut = tutorial.objects.get(pk=pk)
    context = {
	'Tut': Tut,
	}
    return  render(request, 'video.html', context)



def events(request):
    data = EventsModel.objects.all()
    return render(request,'events.html',{'data':data})

from asgiref.sync import async_to_sync
def test(request):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "notification_broadcast",
        {
            'type': 'send_notification',
            'message': json.dumps("Notification")
        }
    )
    return HttpResponse("Done")

# Create your views here.


