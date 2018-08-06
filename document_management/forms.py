from django import forms
from .models import Document

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
