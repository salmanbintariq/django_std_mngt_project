from django import forms
from .models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = ['fname', 'lname', 'email', 'department',]
        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}),
            'department': forms.Select(attrs={'class': 'form-control'}),
        }