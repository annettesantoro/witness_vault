from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from random import randint
from django.views.generic import TemplateView
# Create your views here.

def timeout(request):
    return render(request,
                  'core/timeout.html',
                  {'title': 'Time Out'})

def login(request):
    return render(request,
                  'core/login.html',
                  {'title': 'Log In'})                  

def logout(request):
    return render(request,
                  'core/logout.html',
                  {'title': 'Log Out'})

def home(request):
    return render(request,
                  'core/index.html',
                  {'title': 'Home'})

def welcome(request):
    return render(request,
                  'core/welcome.html',
                  {'title': 'Welcome'})