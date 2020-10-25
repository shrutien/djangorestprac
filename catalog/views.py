from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from .forms import EmployeeForm, SignUpForm
# Create your views here.

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            redirect('dashboard')
    return render(request,'catalog/login.html',{})


def home(request):
    return render(request,'catalog/home.html',{})

def dashboard(request):
    return render(request,'catalog/index.html',{})

def register(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        print('form is valid-----')
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request,'Account created successfully!')
        return redirect('dashboard')
    return render(request,'catalog/register.html',{'form': form})


    