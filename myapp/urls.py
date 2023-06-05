from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot/',views.forgot,name='forgot'),
    path('profile/',views.profile,name="profile"),
    path('reg/',views.register,name='register'),
]