from django import forms
from .models import Witness, Activity, Document, Interaction

#################
#  WITNESS FORM #
#################

class WitnessForm(forms.ModelForm):
    general = (('', '',),
    ('Yes', 'Yes'),
    ('No', 'Now'))
    gender = (('', '',),
    ('Female', 'Female'),
    ('Male', 'Male'))    
    witness_type = (('', '',),
    ('Character Witness', 'Character Witness'),
    ('Eye Witness', 'Eye Witness'),
    ('To be Determined', 'To be Determined'))
    mechanism = (('', '',),
    ('Audio Surveillance', 'Audio Surveillance'),
    ('Both Audio and Visual Surveillance', 'Both Audio and Visual Surveillance'),
    ('To be Determined', 'To be Determined'),
    ('Visual Surveillance', 'Visual Surveillance'))
    witness_status = (('', '',),
    ('New', 'New'),
    ('Under Assesment', 'Under Assessment'),
    ('Verified', 'Verified'),
    ('Unable to Locate', 'Unable to Locate'))
    relationship = (('', '',),
    ('Regultory Officer', 'Regulatory Officer'),
    ('Public', 'Public'),
    ('Employer', 'Employer'),
    ('Worker', 'Worker'),
    ('Unable to Determine', 'Unable to Determine'),            
    ('Other, NEC', 'Other, NEC'))
    case_status = (('', '',),
    ('Active', 'Active'),
    ('Closed', 'Closed'))    
    witness_number = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)
    witness_type = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=witness_type
            ),
            required=False)
    status = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=witness_status
            ),
            required=False)
    gender = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=gender
            ),
            required=False)            
    relationship = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=relationship
            ),
            required=False)
    mechanism = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=mechanism
            ),
            required=False)
    statement = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=general
            ),
            required=False)              
    case = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)    
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)
    dob = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control datepicker',
                'placeholder': 'mm/dd/yyyy'
                }), required=False
                )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)  
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)  
    province = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)  
    country = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)  
    pc = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)  
    primary_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)  
    alternate_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)              
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)
    manager_department = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)
    manager_assignee = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)
    coordinator_department = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)
    coordinator_assignee = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control',
            'placeholder': 'Last Name, First Name'}),
            required=False)
    investigator = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)
    case_status = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=case_status
            ),
            required=False)
    class Meta:
        model = Witness
        fields = ('witness_number', 'witness_type', 'status', 'mechanism', 'case', 'first_name', 'middle_name', 'last_name', 
        'dob', 'gender', 'address', 'city', 'province', 'country', 'pc', 'primary_phone', 'alternate_phone', 'email', 
        'manager_department', 'manager_assignee', 'coordinator_department', 'coordinator_assignee', 'relationship', 'investigator', 'case_status')                    

#################
#  ACTIVITY FORM #
#################


class ActivityForm(forms.ModelForm):
    activity_status = (('Inactive', 'Inactive',),
        ('Pending', 'Pending',),
        ('In Progress', 'In Progress',),
        ('Completed', 'Completed',),
        ('Cancelled', 'Cancelled'))
    lifecycle_status = (('Inactive', 'Inactive',),
        ('Active', 'Active',))        
    activity_type = (('', '',),
        ('Planning', 'Planning'),
        ('Execution', 'Execution'),
        ('Close Down', 'Close Down'))
    priority = (('', '',),
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'))        
    activity_type = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=activity_type
            ),
            required=False)
    priority = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=priority
            ),
            required=False)            
    activity_status = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=activity_status
            ),
            required=False)            
    lifecycle_status = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=lifecycle_status
            ),
            required=False)   
    sequence = forms.CharField(
        widget=forms.NumberInput(
        attrs={'class': 'form-control number'}),
        required=False
        )
    summary = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False
        )
    description = forms.CharField(
        widget=forms.Textarea(
        attrs={'class': 'form-control summernote'}),
        required=False
        )
    manager_assignee = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False
        )
    coordinator_assignee = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control'}),
        required=False
        )
    act_start_date = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control datepicker', 'placeholder': 'mm/dd/yyyy'}),
        required=False)
    act_start_time = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control time', 'placeholder': 'HH:MM'}),
        required=False)
    act_end_date = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control datepicker', 'placeholder': 'mm/dd/yyyy'}),
        required=False)
    act_end_time = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control time', 'placeholder': 'HH:MM'}),
        required=False)
    sched_start_date = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control datepicker', 'placeholder': 'mm/dd/yyyy'}),
        required=False)
    sched_start_time = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control time', 'placeholder': 'HH:MM'}),
        required=False)
    sched_end_date = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control datepicker', 'placeholder': 'mm/dd/yyyy'}),
        required=False)
    sched_end_time = forms.CharField(
        widget=forms.TextInput(
        attrs={'class': 'form-control time', 'placeholder': 'HH:MM'}),
        required=False)
    class Meta:
        model = Activity
        fields =  ('sequence', 'activity_number', 'activity_type', 'activity_status', 'lifecycle_status', 'act_start_date', 'act_start_time', 'sched_start_date', 'sched_start_time',
        'act_end_date', 'act_end_time', 'sched_end_date', 'sched_end_time', 'summary', 'description', 'priority', 'parent_id', 'manager_assignee',
        'coordinator_assignee')

#################
#  DOCUMENTFORM #
#################


class DocumentForm(forms.ModelForm):
    document_type = (('', '',),
    ('Application', 'Application',),
    ('Engineering Assessment', 'Engineering Assessment'),
    ('Engineering Drawing', 'Engineering Drawing'),
    ('Environmental Assessment', 'Environmental Assessment'),
    ('General Correspondence', 'General Correspondence'),
    ('Inspection Report', 'Inspection Report'),
    ('MSDS', 'MSDS'),
    ('Other Document, NEC', 'Other Document, NEC'),
    ('Permit', 'Permit'),
    ('Photographs', 'Photographs'),
    ('Procedure', 'Procedure'),
    ('Regulatory Order', 'Regulatory Order'),
    ('Witness Statement', 'Witness Statement'))
    status = (('New', 'New',),
    ('Active', 'Active'),
    ('Archive', 'Archive'))
    parent_id = forms.ModelChoiceField(
            queryset=Document.objects.all(),
            widget=forms.Select(attrs={'class': 'form-control'}),
            empty_label='', 
            required=False)
    document_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
            required=False
            )
    document_type = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=document_type)
            )                        
    author = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False
            )
    status = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=status)
            )
    issued_date = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control datepicker',
            'placeholder': 'mm/dd/yyyy'}),
            required=False
            )
    received_date = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control datepicker',
            'placeholder': 'mm/dd/yyyy'}),
            required=False
            )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control summernote'}),
            required=False
            )
    summary = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
            )
    attachment = forms.FileField(required=False)

    class Meta:
        model = Document
        fields = ('parent_id', 'document_type', 'status',
                  'issued_date', 'author', 'description', 'attachment', 
                  'document_number', 'received_date', 'issued_date')

#################
#  INTERACTIONFORM #
#################

class InteractionForm(forms.ModelForm):
    status = (('', '',),
    ('Submitted', 'Submitted'),
    ('Delete', 'Delete'))    
    direction = (('', '',),
    ('Inbound', 'Inbound'),
    ('Outbound', 'Outbound'))
    interaction_type = (('', '',),
    ('Acolade', 'Acolade'),    
    ('Complaint', 'Complaint'),
    ('Provide Information', 'Provide Information'),
    ('Request Information', 'Request Information'),        
    ('Other, NEC', 'Other, NEC'))    
    interaction_method = (('', '',),
    ('Phone', 'Phone'),
    ('Social Media', 'Social Media'),
    ('Text', 'Text'))
    relationship = (('', '',),
    ('Aunty', 'Aunty'),
    ('Brother', 'Brother'),
    ('Co-worker', 'Co-Worker'),        
    ('Father', 'Father'),
    ('Grandmother', 'Grandmother'),
    ('Grandfather', 'Grandfather'),            
    ('Mother', 'Mother'),
    ('Other', 'Other'),            
    ('Sister', 'Sister'),
    ('Supervisor', 'Supervisor'),    
    ('No relationship', 'No Relationship'))    
    relationship = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=relationship
            ),
            required=False)
    direction = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=direction
            ),
            required=False)
    interaction_type = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=interaction_type
            ),
            required=False)
    interaction_method = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=interaction_method
            ),
            required=False)
    interaction_date = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control datepicker'})
            )
    interactor = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False
            )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False
            )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False
            )
    summary = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'})
            )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control summernote'}),
            required=False
            )
    status = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=status
            ),
            required=False)
    attachment = forms.FileField(required=False)            
    class Meta:
        model = Interaction
        fields = ('phone', 'email', 'interaction_date', 'interaction_type',
                  'interaction_method', 'summary', 'attachment', 'relationship',
                  'description', 'interaction_number', 'direction', 'status')     