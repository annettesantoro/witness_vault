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


]
