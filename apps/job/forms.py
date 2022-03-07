from django import forms

from .models import job, Application

class AddJobForm(forms.ModelForm):
    class Meta:
        model= job
        fields = ['title', 'short_description', 'long_description', 'company_name', 'company_adress', 'company_zipcode', 'company_place', 'company_country', 'company_size', 'company_contrat', 'company_salary']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model= Application
        fields = ['content', 'experience']
