from django.db import models
from witness_management.models import Witness

# Create your models here.

class Interaction(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.CharField(max_length=40, blank=True, null=True)
    interaction_number = models.CharField(max_length=20, blank=True, null=True)
    direction = models.CharField(max_length=40, blank=True, null=True)
    interaction_type = models.CharField(max_length=40, blank=True, null=True)
    interaction_method = models.CharField(max_length=40, blank=True, null=True)
    interactor = models.CharField(max_length=40, blank=True, null=True)                    
    summary = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=60, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)          
    status = models.CharField(max_length=40, blank=True, null=True)    
    created_by = models.CharField(max_length=60, blank=True, null=True)
    created_date = models.CharField(max_length=60, blank=True, null=True)
    interaction_date = models.CharField(max_length=60, blank=True, null=True)
    relationship = models.CharField(max_length=80, blank=True, null=True)                          

def create(self):
    self.save()

def __str__(self):
    return'{}'.format(self.id)