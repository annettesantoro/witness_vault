from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        r'^witness_workbench/$',
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
    
#    url(
#        r'^new_activity$',
#        views.new_activity,
#        name='new_activity'),
    
    url(r'modify_activity/(?P<pk>\d+)/$',
        views.modify_activity,
        name='modify_activity'),


    url(r'^$',
        views.document_repository,
        name='document_repository'),

#    url(r'^new_document$',
#        views.new_document,
#        name='new_document'),

    url(r'modify_document/(?P<pk>\d+)/$',
        views.modify_document,
        name='modify_document'),

    url(r'^$',
        views.interaction_repository,
        name='interaction_repository'),

#    url(r'^new_interaction/$',
#        views.new_interaction,
#        name='new_interaction'),

    url(r'^modify_interaction/(?P<pk>\d+)/$',
        views.modify_interaction,
        name='modify_interaction'),
]
