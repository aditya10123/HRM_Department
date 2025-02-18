from django.urls import path
from .import views

urlpatterns = [
     path('add',views.add,name="add"),
     path('',views.home,name="home"),
     path('delete/<int:id>/', views.delete_product, name='deleteprod'), 
     path('updateprod/<int:id>/',views.updateprod,name='updateprod'),    
     path('register/',views.register,name="register"),
     path('login/',views.logindetails,name="login"),
     path('logout1/',views.logout_details,name="logout1"),
     path('roles/',views.roles,name="roles"),
     path('deleterole/<int:id>/', views.deleterole, name='deleterole'), 
     path('updaterole/<int:id>/',views.updaterole,name='updaterole'),
     path('employees/', views.create_employee, name='employee_list'),
    path('delete_employee/<int:emp_id>/',views.delete_employee,name='delete_employee'),
     path('update_emp/<int:emp_id>/', views.update_employee, name='update_emp')


]

