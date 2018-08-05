from django.db import models

# Create your models here.

class Witness(models.Model):
    id = models.AutoField(primary_key=True)
    case = models.CharField(max_length=20, blank=True, null=True)
    witness_number = models.CharField(max_length=20, blank=True, null=True)
    witness_type = models.CharField(max_length=80, blank=True, null=True)
    mechanism = models.CharField(max_length=80, blank=True, null=True)
    relationship = models.CharField(max_length=80, blank=True, null=True)        
    status = models.CharField(max_length=40, blank=True, null=True)
    status_reason = models.CharField(max_length=40, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True )
    full_name = models.CharField(max_length=80, blank=True, null=True)
    dob = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    address = models.CharField(max_length=120, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)        
    province = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    pc = models.CharField(max_length=20, blank=True, null=True)
    primary_phone = models.CharField(max_length=20, blank=True, null=True)
    alternate_phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=120, blank=True, null=True)
    manager_department = models.CharField(max_length=60, blank=True, null=True)
    manager_assignee = models.CharField(max_length=80, blank=True, null=True)
    coordinator_department = models.CharField(max_length=80, blank=True, null=True)
    coordinator_assignee = models.CharField(max_length=80, blank=True, null=True)
    created_by = models.CharField(max_length=80, blank=True, null=True)
    created_date = models.CharField(max_length=80, blank=True, null=True)
    statement = models.CharField(max_length=10, blank=True, null=True)
    investigator = models.CharField(max_length=100, blank=True, null=True)
    case_status = models.CharField(max_length=30, blank=True, null=True)                          

def create(self):
    self.save()

def __str__(self):
    return'{}'.format(self.witness_id)            