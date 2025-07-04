from django import forms
from .models import Works,Lives
 
class WorksForm(forms.ModelForm):
    class Meta:
        model=Works
        fields=['person_name','company_name','salary']

class CompanySearchForm(forms.ModelForm):
    company_name=forms.CharField(max_length=100,label='Enter Company name')