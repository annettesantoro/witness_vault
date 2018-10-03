from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),

    url(
        r'^$', 
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
