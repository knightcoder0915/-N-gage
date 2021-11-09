from django.shortcuts import render,redirect
from .models import DeleteModel,EventsModel
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from ngage.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from random import randrange

def user_signup(request):
	if request.method == "POST":
		un = request.POST.get("un")
		try:
			usr = User.objects.get(username=un)
			return render(request,"user_signup.html",{"msg":"email already registered"})
		except User.DoesNotExist:
			pw = ""
			text = "abcdefghijklmnopqrstuvwxyz123456789"
			for i in range(5):
				pw = pw + text[randrange(len(text))]
			print(pw)
			sub = "Welcome to 'N'gage a Nomura Fitness Community"
			msg = "Your password is " + str(pw)
			sender = EMAIL_HOST_USER
			receiver = [str(un)]
			send_mail(sub,msg,sender,receiver)
			usr = User.objects.create_user(username=un,password=pw)
			usr.save()
			return redirect("user_login")
	else:
		return render(request,"user_signup.html")

def user_login(request):
	if request.method == "POST":
		un = request.POST.get("un")
		pw = request.POST.get("pw")
		usr = authenticate(username=un,password=pw)
		if usr is None:
			return render(request,"user_login.html",{"msg":"invalid login"})
		else:
			login(request,usr)
			return redirect("index")
	else:
		return render(request,"user_login.html")

def user_logout(request):
	logout(request)
	return redirect("user_login")

def user_np(request):
	if request.method == "POST":
		un = request.POST.get("un")
		try:
			usr = User.objects.get(username=un)
			pw = ""
			text = "abcdefghijklmnopqrstuvwxyz123456789"
			for i in range(5):
				pw = pw + text[randrange(len(text))]
			print(pw)
			sub = "Welcome to 'N'gage a Nomura Fitness Community"
			msg = "Your password is " + str(pw)
			sender = EMAIL_HOST_USER
			receiver = [str(un)]
			send_mail(sub,msg,sender,receiver)
			usr.set_password(pw)
			usr.save()
			return redirect("user_login")
		except User.DoesNotExist:
			return render(request,"user_signup.html",{"msg":"email not registered"})
	else:
		return render(request,"user_np.html")


def ulogin(request):
	if request.method == 'POST':
		un = request.POST.get('un')
		pw = request.POST.get('pw')
		#print(un,pw)
		usr = authenticate(username=un,password=pw)
		if usr is None:
			return render(request,'ulogin.html',{'msg':'invalid credentials'})
		else:
			login(request,usr)
			return redirect('hrhome')
	else:
		return render(request,'ulogin.html')

def ucreate(request):
	if request.method == "POST":
		fn = request.POST.get("fn")
		ln = request.POST.get("ln")
		em = request.POST.get("em")
		un = em
		try:
			usr =  User.objects.get(username=un) and User.objects.get(email=em)
			print(usr)
			return render(request , 'ucreate.html' , {'msg':'Employee Already Registered'})
		except User.DoesNotExist:
			text = "1234567890abcdefghijklmnopqrstuvwxyz"
			pw = ""
			for i in range(6):
				pw = pw + text[randrange(len(text))]
			print(pw)
			send_mail("Welcome to Nomura Fitness  " , "Your password is " + pw , EMAIL_HOST_USER,[em])
			usr = User.objects.create_user(username = un , password=pw,email=em)
			usr.first_name = fn
			usr.last_name = ln
			usr.save()
			return render(request , 'ucreate.html' , {'msg':'Employee Created'})
	else:
		return render(request,'ucreate.html')

def delete(request,id):
	ds = User.objects.get(username = id)
	del_emp = ds.username
	del_hr = request.user.username
	d = DeleteModel(deleted_Employee= del_emp,deleting_HR = del_hr)
	d.save()
	ds.delete()
	return redirect('hrhome')

def cevent(request):
	if request.method == "POST":
		ename = request.POST.get('ename')
		edesc = request.POST.get('edesc')
		edate = request.POST.get('edate')
		eurl = request.POST.get('eurl')
		d = EventsModel(ename=ename,description=edesc,date_of_event=edate,image_url=eurl)
		d.save()
		return render(request,'cevent.html',{'msg':'Event Created'})
	else:
		
		return render(request,'cevent.html')

def devent(request):
	if request.method == "POST":
		ename = request.POST.get('ename')
		ds = EventsModel.objects.get(ename = ename)
		ds.delete()
		return redirect('cevent')
	else:
		return render(request,'devent.html')



def ulogout(request):
	logout(request)
	return redirect('ulogin')

