from django import forms
from .models import *
#from django_select2.forms import Select2Widget

class VirusForm(forms.Form):
    viruses = forms.ModelChoiceField(
        queryset=virus.objects.values_list('name', flat=True))

class OrganismForm(forms.Form):
    organisms = forms.ModelChoiceField(
        queryset=organism.objects.values_list('name', flat=True))

class SiteForm(forms.Form):
    sites = forms.ModelChoiceField(
    queryset=site.objects.values_list('name', flat=True))