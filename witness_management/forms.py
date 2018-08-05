from django import forms
from .models import Witness
from document_management.forms import DocumentForm
from interaction_management.forms import InteractionForm

class WitnessForm(forms.ModelForm):
    witness_status = (('', '',),
    ('New', 'New'),
    ('Under Assessment', 'Under Assessment'),
    ('Verified', 'Verified'))
    witness_type = (('', '',),
    ('Character Witness', 'Character Witness'),
    ('Eye Witness', 'Eye Witness'),
    ('To be Determined', 'To be Determined'))
    mechanism = (('', '',),
    ('Audio Surveillance', 'Audio Surveillance'),
    ('Both Audio and Visual Surveillance', 'Both Audio and Visual Surveillance'),
    ('To be Determined', 'To be Determined'),
    ('Visual Surveillance', 'Visual Surveillance'))
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
    witness_mechanism = forms.CharField(
        widget=forms.Select(
            attrs={'class': 'form-control'},
            choices=mechanism
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
            attrs={'class': 'form-control'}),
            required=False)
    gender = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}),
            required=False)  
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
            attrs={'class': 'form-control'}),
            required=False)

    class Meta:
        model = Witness
        fields = ('witness_number', 'witness_type', 'status', 'mechanism', 'case', 'first_name', 'middle_name', 'last_name', 
        'dob', 'gender', 'address', 'city', 'province', 'country', 'pc', 'primary_phone', 'alternate_phone', 'email', 
        'manager_department', 'manager_assignee', 'coordinator_department', 'coordinator_assignee')                    
