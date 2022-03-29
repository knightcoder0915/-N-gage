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

def recommendation(request):
	if request.method == "POST":
		ht = float(request.POST.get("height"))
		wt = float(request.POST.get("weight"))
		bmi = (wt) / (ht * ht)
		bmi = round(bmi,2)
		if bmi < 18  :
			return render(request,"recommendation.html",{"msg": "Your BMI is " + str(bmi) + " .\n   We recommend you Yoga. You can check our playlists."})
		elif bmi > 18 and bmi <= 22:
			return render(request,"recommendation.html",{"msg": "Your BMI is " + str(bmi) + ".\n We recommend you HIIT Workouts. You can check our playlists."})
		else:
			return render(request,"recommendation.html",{"msg":"Your BMI is " + str(bmi) + ".\n We recommend you Cardio Training. You can check our playlists."})
	else:
		return render(request,'recommendation.html')


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


