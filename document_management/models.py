from django.db import models

# Create your models here.

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.CharField(max_length=20, blank=True, null=True)
    document_number = models.CharField(max_length=20, blank=True, null=True)
    document_type = models.CharField(max_length=40, blank=True, null=True)  
    summary = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=60, blank=True, null=True)
    author = models.CharField(max_length=60, blank=True, null=True)    
    status = models.CharField(max_length=40, blank=True, null=True)
    issued_date = models.CharField(max_length=40, blank=True, null=True)       
    received_date = models.CharField(max_length=40, blank=True, null=True)          
    created_by = models.CharField(max_length=60, blank=True, null=True)
    created_date = models.CharField(max_length=60, blank=True, null=True)        

def create(self):
    self.save()

def __str__(self):
    return'{}'.format(self.document_id)