from django.conf.urls import url
from . import views

urlpatterns = [

# Interaction URLS
    url(r'^$',
        views.interaction_workbench,
        name='interaction_workbench'),

    url(r'^new_interaction/$',
        views.new_interaction,
        name='new_interaction'),

    url(r'^modify_interaction/(?P<pk>\d+)/$',
        views.modify_interaction,
        name='modify_interaction'),


]
