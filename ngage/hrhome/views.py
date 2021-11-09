
from django.shortcuts import render,redirect
from django.contrib.auth.models import User

def hrhome(request):
	if request.user.is_authenticated:
		data = User.objects.all()
		return render(request,'hrhome.html',{'data':data})
		
	else:
		return redirect('ulogin')
