from django.contrib import admin
from .models import UserDetail, resturants_details
from .models import UserDetail ,Grocery_details

class UserDetailAdmin(admin.ModelAdmin):
    list_display = ("username", "firstname", "lastname",
                    "phone", "email", "password", "confirmpassword")


admin.site.register(UserDetail, UserDetailAdmin)




class rest_details(admin.ModelAdmin):
    list_display = ("item_name", "item_description","items_price")


admin.site.register(resturants_details, rest_details)


class Grocery_detailsAdmin(admin.ModelAdmin):
    list_display=("Grocery_name","Grocery_price","Grocery_description")
admin.site.register(Grocery_details,Grocery_detailsAdmin)