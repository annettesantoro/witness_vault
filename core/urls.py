from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$', 
        views.home, 
        name='home'),

    url(
        r'^home$', 
        views.home, 
        name='home'),

    url(
        r'^$', 
        views.welcome, 
        name='welcome'),

    url(
        r'^$', 
        views.timeout, 
        name='timeout'),
    
    url(
        r'^logout$', 
        views.logout, 
        name='logout'),

    url(
        r'^login$', 
        views.login, 
        name='login'),        
    ]
