from django import forms
from .models import Department
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



class Departmentform(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name','department_description']
        widgets = {
            'department_name' : forms.TextInput(attrs={'class':'form-control'}),
            'department_description' : forms.TextInput(attrs={'class':'form-control'}),
        }

class userauthenticationForm (AuthenticationForm):
    username=forms.CharField(label="Enter username",widget=forms.TextInput(attrs={'class':'form-control'})),
    password=forms.CharField(label="Enter password",widget=forms.PasswordInput(attrs={'class':'form-control'})),   
    
    class Meta:
        model=User
        fields=['username','password']

class registrationform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
        
        labels={
            'username':'Enter Username',
            'first_name':'Enter first name',
            'last_name':'Enter Last name',
            'email':'Enter Email',
            'password1':'Enter password',
            'password2':'Enter confirm password',
        }
        
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        }
 

class loginform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password']
        
        labels={
            'username':'Enter Username',
            'password':'Enter password',
        }
        
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
        }