# from django.urls import pa
from . import views

urlpatterns = [
    path('updateprofile',views.updateprofile,name='updateprofile'),
]
