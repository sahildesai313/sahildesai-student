from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgot/',views.forgot,name='forgot'),
    path('profile/',views.profile,name="profile"),
    path('reg/',views.register,name='register'),
    path('home/',views.homepage,name='home'),
    path('home/rest_detail/<int:image_id>/',views.rest,name='rest'),
     path('home/grocery_details/<int:image_id>/',views.grocery,name='grocery'),
     path('tour/<int:id>/',views.tour,name='tour'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

