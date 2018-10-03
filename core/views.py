
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from random import randint
from django.views.generic import TemplateView
# Create your views here.


# Home #
########
def timeout(request):
    return render(request,
                  'core/timeout.html',
                  {'title': 'Time Out'})

def logout(request):
    return render(request,
                  'core/logout.html',
                  {'title': 'Log Out'})

# Home #
########
def home(request):
    return render(request,
                  'core/index.html',
                  {'title': 'Home'})


@login_required(login_url='/login/')
def welcome(request):
    return render(request,
                  'core/welcome.html',
                  {'title': 'Welcome'})