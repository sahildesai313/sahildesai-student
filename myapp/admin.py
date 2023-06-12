from django.contrib import admin
from .models import UserDetail, resturants_details,Grocery_details,Package_details


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


class Package_Details(admin.ModelAdmin):
    list_display = ("package_name","admin_image","package_image","no_of_day","package_description","package_price")
admin.site.register(Package_details,Package_Details)


