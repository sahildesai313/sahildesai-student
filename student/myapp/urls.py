from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('reg/',views.registerpage,name='reg'),
    path('login/',views.login,name='login'),
    path('logout',views.Logout,name="logout")
]
