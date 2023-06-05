from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot/',views.forgot,name='forgot')
=======

    path('reg/',views.register,name='register'),
>>>>>>> 854ce4737f84042e2ce552af5a0d187ee630dec1
]