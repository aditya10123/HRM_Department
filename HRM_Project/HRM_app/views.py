from django.shortcuts import render,redirect,get_object_or_404
from .forms import Departmentform,userauthenticationForm,registrationform,Rolesform
from .models import Department,Roles
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required


# Create your views here.
def add(request):
    departments = Department.objects.filter(status=True)

    if request.method == 'POST':
        fm = Departmentform(request.POST)
        if fm.is_valid():
            dn=fm.cleaned_data['department_name']
            dd=fm.cleaned_data['department_description']
            reg = Department(department_name=dn,department_description=dd)
            reg.save()
            fm = Departmentform()  
    else:
        departments = Department.objects.filter(status=True)
        fm = Departmentform()   
        
    return render(request, 'add.html',{'form':fm, 'deprt':departments})

def home(request):
    return render(request,'home.html')



import datetime
def logindetails(request):
    if request.method=="POST":
        uname=request.POST["username"]
        upass=request.POST["password"]
        user=authenticate(request,username=uname,password=upass)
        
        if user is not None:
            login(request,user)
            response=redirect('home')
            request.session['username']=uname
            response.set_cookie('username',uname)
            response.set_cookie('time',datetime.datetime.now())
            return response
        else:
            LDF=userauthenticationForm()
            return render(request,"login.html",{"LDF":LDF,'msg':'Worong password or username...!'})
    else:
        LDF=userauthenticationForm()
        return render(request,"login.html",{"LDF":LDF})
    
def logout_details(request):
    logout(request)
    return redirect('home')

def delete_product(request, id):
    deletedept = Department.objects.get(id=id)
    print('got', deletedept)
    deletedept.status = False
    deletedept.save()
    print() 
    fm = Departmentform()   
    return redirect('add')
 
    
 


def updateprod(request, id):
    # Safely get the department object or return a 404 if not found
    product = get_object_or_404(Department, id=id)
    
    if request.method == "POST":
        form = Departmentform(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('add')
        else:
            # Return the form with errors to the template
            return render(request, "update.html", {"form": form})
    else:
        # Initialize the form with the existing product instance
        form = Departmentform(instance=product)
        return render(request, "update.html", {"form": form})


def register(request):
    if request.method=="POST":
        RF=registrationform(request.POST)
        if RF.is_valid():
            RF.save()
            return redirect('home')
        else:
            RF=registrationform()
            return render(request,"register.html",{"RF":RF,'msg':'Worong credentials...!'})
    else:
        RF=registrationform()
        return render(request,"register.html",{"RF":RF})
    



def roles(request):
    role = Roles.objects.filter(status=True)

    if request.method == 'POST':
        fm = Rolesform(request.POST)
        if fm.is_valid():
            dn=fm.cleaned_data['role_name']
            dd=fm.cleaned_data['role_description']
            reg = Roles(role_name=dn,role_description=dd)
            reg.save()
            fm = Rolesform()  
    else:
        role = Roles.objects.filter(status=True)
        fm = Rolesform()   
        
    return render(request, 'roles.html',{'form':fm, 'role':role})


def deleterole(request, id):
    deleterole = Roles.objects.get(id=id)
    print('got', deleterole)
    deleterole.status = False
    deleterole.save()
    print() 
    fm = Rolesform()   
    return redirect('roles')
 

def updaterole(request, id):
    # Safely get the department object or return a 404 if not found
    role = get_object_or_404(Roles, id=id)
    
    if request.method == "POST":
        form = Rolesform(request.POST, request.FILES, instance=role)
        if form.is_valid():
            form.save()
            return redirect('roles')
        else:
            # Return the form with errors to the template
            return render(request, "updaterole.html", {"form": form})
    else:
        # Initialize the form with the existing product instance
        form = Rolesform(instance=role)
        return render(request, "updaterole.html", {"form": form})
