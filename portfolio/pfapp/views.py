from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Contact

# Create your views here.

# Home/Index View


def index(request):
    # Check Post Method And Request Type
    if request.method == 'POST' and request.is_ajax():
        # Check For Empty Name Field
        if request.POST['name'] == '':
            username = 'Arnab Gupta'  # Set Default Username
        else:
            username = request.POST['name']
        # Check For Select Field
        if request.POST['gender'] == "select":
            gender = 'M'
        else:
            gender = request.POST['gender']
        return HttpResponse(json.dumps({'name': username, 'gender': gender}))
    else:
        return render(request, 'pfapp/index.html')

# Portfolio View


def portfolio(request):
    return render(request, 'pfapp/portfolio.html')

# Contact View


def contact(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        form = Contact(email=email, subject=subject, message=message)
        form.save()

        return render(request, 'pfapp/contact.html')
    else:
        return render(request, 'pfapp/contact.html')
