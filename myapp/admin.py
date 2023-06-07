from django.contrib import admin
from .models import UserDetail ,package_details


class UserDetailAdmin(admin.ModelAdmin):
    list_display = ("username", "firstname", "lastname",
                    "phone", "email", "password", "confirmpassword")
admin.site.register(UserDetail, UserDetailAdmin)


class Package_Details(admin.ModelAdmin):
    list_display = ("package_name","no_of_day","package_description","package_price","image")
admin.site.register(package_details,Package_Details)

