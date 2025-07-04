from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    dob = forms.DateField(label="Date of Birth", widget=forms.DateInput(attrs={'type': 'date'}))
    address = forms.CharField(widget=forms.Textarea, label="Address")
    contact = forms.CharField(label="Contact Number", max_length=15)
    email = forms.EmailField(label="Email ID")
    english = forms.IntegerField(label="English Marks", min_value=0, max_value=100)
    physics = forms.IntegerField(label="Physics Marks", min_value=0, max_value=100)
    chemistry = forms.IntegerField(label="Chemistry Marks", min_value=0, max_value=100)
    SST=forms.IntegerField(label="SST",min_value=0,max_value=100)
    Arabic=forms.IntegerField(label="Arabic",min_value=0,max_value=100)
