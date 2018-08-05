from django.conf.urls import url
from . import views

urlpatterns = [

url(r'^$',
    views.document_workbench,
    name='document_workbench'),

url(r'^new_document$',
    views.new_document,
    name='new_document'),

url(r'modify_document/(?P<pk>\d+)/$',
    views.modify_document,
    name='modify_document'),
]
