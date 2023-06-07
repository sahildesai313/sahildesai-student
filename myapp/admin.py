from django.contrib import admin
from .models import UserDetail,Package_details


class UserDetailAdmin(admin.ModelAdmin):
    list_display = ("username", "firstname", "lastname",
                    "phone", "email", "password", "confirmpassword")


admin.site.register(UserDetail, UserDetailAdmin)


class Package_Details(admin.ModelAdmin):
    list_display = ("package_name","admin_image","package_image","no_of_day","package_description","package_price")
admin.site.register(Package_details,Package_Details)

