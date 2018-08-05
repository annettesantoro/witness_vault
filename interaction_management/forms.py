from django import forms
from .models import Interaction

###############
# Interaction #
###############
class InteractionForm(forms.ModelForm):
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
        widget=forms.Textarea(
            attrs={'class': 'form-control summernote'}),
            required=False
            )        
    attachment = forms.FileField(required=False)            
    class Meta:
        model = Interaction
        fields = ('phone', 'email', 'interaction_date', 'interaction_type',
                  'interaction_method', 'summary', 'attachment',
                  'description', 'interaction_number', 'direction', 'status')     