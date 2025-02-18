from django import forms
from .models import Department,Roles,Employe_User
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


class Rolesform(forms.ModelForm):
    class Meta:
        model = Roles
        fields = ['role_name','role_description']
        widgets = {
            'role_name' : forms.TextInput(attrs={'class':'form-control'}),
            'role_description' : forms.TextInput(attrs={'class':'form-control'}),
        }

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employe_User
        fields = [
            'first_name', 'last_name', 'email', 'mobile', 'role', 'dept', 
            'reporting_manager', 'date_of_joining', 'username', 'password'
        ]
        
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter a secure password'}),
            'date_of_joining': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
        }

    # First Name
    first_name = forms.CharField(
        max_length=50, 
        required=True, 
        label="First Name", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter first name'})
    )
    
    # Last Name
    last_name = forms.CharField(
        max_length=50, 
        required=True, 
        label="Last Name", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter last name'})
    )
    
    # Email
    email = forms.EmailField(
        max_length=50, 
        required=True, 
        label="Email", 
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email address'})
    )
    
    # Mobile Number
    mobile = forms.CharField(
        max_length=50, 
        required=True, 
        label="Mobile Number", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter mobile number'})
    )
    
    # Role
    role = forms.ModelChoiceField(
        queryset=Roles.objects.all(), 
        required=True, 
        label="Select Role", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Department
    dept = forms.ModelChoiceField(
        queryset=Department.objects.all(), 
        required=True, 
        label="Select Department", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Reporting Manager (Optional)
    reporting_manager = forms.ModelChoiceField(
        queryset=Employe_User.objects.all(), 
        required=False, 
        label="Allocate Reporting Manager", 
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Date of Joining
    date_of_joining = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'placeholder': 'YYYY-MM-DD'}),
        label="Date of Joining"
    )
    
    # Username
    username = forms.CharField(
        max_length=50, 
        required=True, 
        label="Username", 
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )
    
    # Password
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Set a strong password', 'class': 'form-control'}), 
        required=True, 
        label="Set Password",
        min_length=8,
        help_text="Password must be at least 8 characters long"
    )

    # You can add custom error messages as well
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Employe_User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already taken.")
        return email