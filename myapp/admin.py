from django.contrib import admin
from .models import UserDetail


class UserDetailAdmin(admin.ModelAdmin):
    list_display = ("username", "firstname", "lastname",
                    "phone", "email", "password", "confirmpassword")


admin.site.register(UserDetail, UserDetailAdmin)
