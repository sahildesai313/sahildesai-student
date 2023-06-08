from django.contrib import admin
from .models import UserDetail, resturants_details


class UserDetailAdmin(admin.ModelAdmin):
    list_display = ("username", "firstname", "lastname",
                    "phone", "email", "password", "confirmpassword")


admin.site.register(UserDetail, UserDetailAdmin)




class rest_details(admin.ModelAdmin):
    list_display = ("item_name", "item_description","items_price")


admin.site.register(resturants_details, rest_details)
