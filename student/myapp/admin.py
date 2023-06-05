from django.contrib import admin
from .models import Register

    
class RegisterAdmin(admin.ModelAdmin):
  list_display = ("username","firstname", "lastname","phone","email","password","confirmpassword")
  

  


admin.site.register(Register,RegisterAdmin)