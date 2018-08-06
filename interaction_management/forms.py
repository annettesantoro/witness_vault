from django import forms
from .models import Interaction

###############
# Interaction #
###############
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