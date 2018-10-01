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
        return'{}'.format(self.witness_number) 

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    sequence = models.CharField(max_length=6, blank=True, null=True)
    priority = models.CharField(max_length=10, blank=True, null=True)                
    parent_id = models.CharField(max_length=20, blank=True, null=True)
    activity_number = models.CharField(max_length=6, blank=True, null=True)    
    summary = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    activity_type = models.CharField(max_length=80, blank=True, null=True)     
    activity_status = models.CharField(max_length=20, blank=True, null=True)
    lifecycle_status = models.CharField(max_length=20, blank=True, null=True)
    req_start_date = models.CharField(max_length=20, blank=True, null=True)
    req_start_time = models.CharField(max_length=20, blank=True, null=True)
    req_end_date = models.CharField(max_length=20, blank=True, null=True)
    req_end_time = models.CharField(max_length=20, blank=True, null=True)           
    sched_start_date = models.CharField(max_length=20, blank=True, null=True)
    sched_start_time = models.CharField(max_length=20, blank=True, null=True)
    sched_end_date = models.CharField(max_length=20, blank=True, null=True)
    sched_end_time = models.CharField(max_length=20, blank=True, null=True)
    act_start_date = models.CharField(max_length=20, blank=True, null=True)        
    act_start_time = models.CharField(max_length=20, blank=True, null=True)
    act_end_date = models.CharField(max_length=20, blank=True, null=True)
    act_end_time = models.CharField(max_length=20, blank=True, null=True)
    manager_assignee = models.CharField(max_length=120, blank=True, null=True)
    coordinator_assignee = models.CharField(max_length=120, blank=True, null=True)
    created_by = models.CharField(max_length=80, blank=True, null=True)
    created_date = models.CharField(max_length=80, blank=True, null=True)
    modified_by = models.CharField(max_length=80, blank=True, null=True)
    modified_date = models.CharField(max_length=80, blank=True, null=True)

    def create(self):
        self.save()

    def __str__(self):
        return'{}'.format(self.activity_number)

class Document(models.Model):
    id = models.AutoField(primary_key=True)
    parent_id = models.CharField(max_length=20, blank=True, null=True)
    document_number = models.CharField(max_length=20, blank=True, null=True)
    document_type = models.CharField(max_length=40, blank=True, null=True)  
    summary = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=60, blank=True, null=True)
    author = models.CharField(max_length=60, blank=True, null=True)    
    status = models.CharField(max_length=40, blank=True, null=True)
    issued_date = models.CharField(max_length=40, blank=True, null=True)       
    received_date = models.CharField(max_length=40, blank=True, null=True)          
    created_by = models.CharField(max_length=60, blank=True, null=True)
    created_date = models.CharField(max_length=60, blank=True, null=True)        

    def create(self):
        self.save()

    def __str__(self):
        return'{}'.format(self.document_number)

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