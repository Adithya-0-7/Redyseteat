from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from .models import fooditem
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def food_items_view(request):
    items = fooditem.objects.all()
    return render(request, 'index.html', {'items': items})


def landingpage(request):
    return render(request,'landingpage.html')
@login_required
def home(request):
    items = fooditem.objects.all()
    return render(request, 'index.html',{'items':items})
def signup_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request, 'signup.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

@login_required
def logout_page(request):
    logout(request)
    return redirect('landingpage')
