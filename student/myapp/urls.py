from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot/',views.forgot,name='forgot')
]