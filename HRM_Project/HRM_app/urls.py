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
     path('update_emp/<int:emp_id>/', views.update_employee, name='update_emp'),
     path('forget_password/',views.forget_password,name='forget_password'),
     path('reset_password/<uidb64>/<token>/',views.reset_password,name='resetpassword'),
     path('password_reset_done/',views.password_reset_done,name='passwordresetdone'),

     path('task_list/', views.task_list, name='task_list'),
     path('task/create/', views.task_create, name='task_create'),
     path('task/update/<int:task_id>/', views.task_update, name='task_update'),
     path('task/delete/<int:task_id>/', views.task_delete, name='task_delete'),
     path('task/assign/', views.assign_task, name='assign_task'),
     
    


     # path('add_review/', views.add_review, name='add_review'),
     # path('review_list/', views.review_list, name='review_list'),
     # path('<int:review_id>/edit/', views.edit_review, name='edit_review'),
     # path('<int:review_id>/delete/', views.delete_review, name='delete_review'),

]

