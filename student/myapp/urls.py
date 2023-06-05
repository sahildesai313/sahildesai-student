from django.urls import path
from . import views

urlpatterns = [
    path('updateprofile',views.updateprofile,name='updateprofile'),
]
