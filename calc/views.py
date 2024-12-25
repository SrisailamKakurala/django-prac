from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .models import User
# Create your views here.

def home(request):
    print(request)
    return render(request, 'home.html', {'name': 'ssl'})

def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1 + val2
    return render(request, 'result.html', {'result': res})

def users(request):
    users = User.objects.all()
    # creating a new user in db
    name='ssl123456789'
    email='ssl@ssl'
    age=20
    if User.objects.filter(name=name).exists():
        # messages.info(request, 'User already exists')
        return HttpResponse('User already exists')
    else:
        newUser = User.objects.create(name=name, email=email, age=age)
        newUser.save()
        return render(request, 'users.html', {'users': users})