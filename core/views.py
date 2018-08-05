from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from random import randint
from django.views.generic import TemplateView
# Create your views here.

def timeout(request):
    return render(request,
                  'home/timeout.html',
                  {'title': 'Time Out'})

def logout(request):
    return render(request,
                  'home/logout.html',
                  {'title': 'Log Out'})

def home(request):
    return render(request,
                  'home/index.html',
                  {'title': 'Home'})

def welcome(request):
    return render(request,
                  'home/welcome.html',
                  {'title': 'Welcome'})