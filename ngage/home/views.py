from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

def home(request):
    if request.method == "POST":
        contact=Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        contact.name=name
        contact.email=email
        contact.subject=subject
        contact.save()
        return render(request,'home.html', {"message":'Thank you for submitting your Query!We will contact you shortly '+contact.name})

    return render(request,"home.html")

# Create your views here.
