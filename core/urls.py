from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    path('', views.home, name='Home'),
    

    url(
        r'^welcome$', 
        views.welcome, 
        name='welcome'),

    url(
        r'^timeout$', 
        views.timeout, 
        name='timeout'),
    
    url(
        r'^logout$', 
        views.logout, 
        name='logout'),

    url(
        r'^login/$', 
        views.login, 
        name='login'),        
    ]
