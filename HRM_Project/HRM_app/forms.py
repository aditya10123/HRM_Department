from django import forms
from .models import Department
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class Departmentform(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['Department_Name','Department_Description']
        widgets = {
            'Department_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Department_Description' : forms.TextInput(attrs={'class':'form-control'}),
        }

class userauthenticationForm (AuthenticationForm):
    username=forms.CharField(label="Enter username",widget=forms.TextInput(attrs={'class':'form-control'})),
    password=forms.CharField(label="Enter password",widget=forms.PasswordInput(attrs={'class':'form-control'})),   
    
    class Meta:
        model=User
        fields=['username','password']
 
    