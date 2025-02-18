from django.shortcuts import render,redirect,get_object_or_404
from .forms import Departmentform,userauthenticationForm,registrationform,Rolesform,EmployeeForm
from .models import Department,Roles,Employe_User
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




# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .models import EmployeeUser
# from .forms import EmployeeForm

# @login_required
# def employee_list(request):
    
#     employees = EmployeeUser.objects.all()

#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             employee = form.save(commit=False)  
              
#             # Ensure reporting_manager is set to an EmployeeUser instance
#             if employee.reporting_manager and isinstance(employee.reporting_manager, EmployeeUser):
#                 employee.reporting_manager = employee.reporting_manager
#             else:
#                 employee.reporting_manager = None  # If invalid, default to None
            
#             employee.save()  # Save the employee instance
#             return redirect('employee_list')  # Redirect after successful submission
#     else:
#         form = EmployeeForm()

#     return render(request, 'employee_list.html', {'form': form, 'employees': employees})


# @login_required
# def employee_update(request, employee_id):
  
#     employee = get_object_or_404(EmployeeUser, pk=employee_id)

#     if request.method == 'POST':
#         form = EmployeeForm(request.POST, instance=employee)
#         if form.is_valid():
#             form.save()
#             return redirect('employee_list')
#     else:
#         form = EmployeeForm(instance=employee)

#     return render(request, 'employee_update.html', {'form': form, 'employee': employee})


# @login_required
# def employee_delete(request, employee_id):
#     employee = get_object_or_404(EmployeeUser, pk=employee_id)
#     if request.method == 'POST':
#         employee.delete()
#         return redirect('employee_list')

#     return render(request, 'employee_confirm_delete.html', {'employee': employee})


# import logging
from django.contrib import messages


# logger = logging.getLogger(__name__)

# def create_employee(request):
#     departments = Department.objects.filter(status=True)
#     roles = Roles.objects.filter(status=True)

#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             employee = form.save(commit=False)

#             # Get the department ID from the POST data
#             department_id = request.POST.get('dept')
#             # Adjust filtering based on the department ID or name
#             department = Department.objects.filter(id=department_id, status=True).first()

#             if not department:
#                 messages.error(request, "Invalid or inactive department selected")
#                 return render(request, 'employee_list.html', {'form': form, 'departments': departments, 'roles': roles})

#             # Get the role from the POST data
#             role_id = request.POST.get('role')
#             role = Roles.objects.filter(id=role_id, status=True).first()

#             if not role:
#                 messages.error(request, "Invalid or inactive role selected")
#                 return render(request, 'employee_list.html', {'form': form, 'departments': departments, 'roles': roles})

#             # Assign the department and role to the employee
#             employee.department = department
#             employee.role = role
#             employee.save()

#             messages.success(request, "Employee created successfully!")
#             return redirect('employee_list')

#     else:
#         form = EmployeeForm()

#     return render(request, 'employee_list.html', {'form': form, 'departments': departments, 'roles': roles})



from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import EmployeeForm
from .models import Employe_User, Department, Roles

def create_employee(request):
    departments = Department.objects.filter(status=True)
    roles = Roles.objects.filter(status=True)
    employees = Employe_User.objects.all()  # ✅ Fetch all employees

    if request.method == "POST":
        print("🚀 Form Data Received:", request.POST)  # Debugging

        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)

            # Validate department
            department_id = request.POST.get('dept')
            department = Department.objects.filter(id=department_id, status=True).first()
            if not department:
                messages.error(request, "Invalid or inactive department selected")
                return render(request, 'employee_list.html', {
                    'form': form, 'departments': departments, 'roles': roles, 'employees': employees
                })

            # Validate role
            role_id = request.POST.get('role')
            role = Roles.objects.filter(id=role_id, status=True).first()
            if not role:
                messages.error(request, "Invalid or inactive role selected")
                return render(request, 'employee_list.html', {
                    'form': form, 'departments': departments, 'roles': roles, 'employees': employees
                })

            # Assign department and role
            employee.department = department
            employee.role = role
            employee.save()

            messages.success(request, "Employee created successfully!")
            return redirect('employee_list')

        else:
            messages.error(request, "Form is invalid. Please check the inputs.")
            print("⚠️ Form Errors:", form.errors)  # Debugging

    else:
        form = EmployeeForm()

    return render(request, 'employee_list.html', {
        'form': form, 'departments': departments, 'roles': roles, 'employees': employees
    })

def delete_employee(request, emp_id):
    employee = get_object_or_404(Employe_User, employee_id=emp_id) 
    print("Employee found:",employee)
    employee.delete()
    print("Employee deleted successfully")
    messages.success(request, "Employee deleted successfully!")
    return redirect('employee_list')

def update_employee(request,emp_id):
    employee = get_object_or_404(Employe_User, employee_id=emp_id)
    if request.method == "POST":
        form =EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        else:
            return render(request, "update_emp.html", {"form": form})
    else:
       
        form = EmployeeForm(instance=employee)
        return render(request, "update_emp.html", {"form": form})

