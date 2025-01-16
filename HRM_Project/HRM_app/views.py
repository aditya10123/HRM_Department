from django.shortcuts import render,redirect,get_object_or_404
from .forms import Departmentform,userauthenticationForm
from .models import Department
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def add(request):
    depart = Department.objects.all()
    if request.method == 'POST':
        fm = Departmentform(request.POST)
        if fm.is_valid():
            dn=fm.cleaned_data['Department_Name']
            dd=fm.cleaned_data['Department_Description']
            reg = Department(Department_Name=dn,Department_Description=dd)
            reg.save()
            fm = Departmentform()  
    else: 
        fm = Departmentform()   
        
    return render(request, 'add.html',{'form':fm, 'deprt':depart})

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
    deleteMenu=Department.objects.filter(id=id)
    deleteMenu.delete()
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
