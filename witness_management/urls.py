from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^$',
        views.witness_workbench,
        name='witness_workbench'),
    
    url(
        r'^new_witness$',
        views.new_witness,
        name='new_witness'),
    
    url(r'modify_witness/(?P<pk>\d+)/$',
        views.modify_witness,
        name='modify_witness'),

    url(
        r'^activity_workbench/$',
        views.activity_workbench,
        name='activity_workbench'),
    
    url(r'modify_activity/(?P<pk>\d+)/$',
        views.modify_activity,
        name='modify_activity'),

    url(r'^document_repository/$',
        views.document_repository,
        name='document_repository'),

    url(r'modify_document/(?P<pk>\d+)/$',
        views.modify_document,
        name='modify_document'),

    url(r'^interaction_repository/$',
        views.interaction_repository,
        name='interaction_repository'),

    url(r'^modify_interaction/(?P<pk>\d+)/$',
        views.modify_interaction,
        name='modify_interaction'),

]
