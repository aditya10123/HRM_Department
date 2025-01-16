from django.urls import path
from .import views

urlpatterns = [
     path('add',views.add,name="add"),
     path('',views.home,name="home"),
     path('login/',views.logindetails,name="login"),
     path('logout_details/',views.logout_details,name="logout_details"),
     path('delete/<int:id>/', views.delete_product, name='deleteprod'), 
     path('updateprod/<int:id>/',views.updateprod,name='updateprod'),    
]
