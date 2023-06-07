from django.db import models

from django.utils.safestring import mark_safe
class UserDetail(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    confirmpassword = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.username}{self.firstname}{self.lastname}{self.phone}{self.email}{self.password}{self.confirmpassword}"


class Package_details(models.Model):
    package_name =models.CharField(max_length=20)
    package_image =models.ImageField(upload_to="photos", default="")
    no_of_day =models.IntegerField(default="")
    package_description =models.TextField(default="")
    package_price=models.IntegerField(default="")

    def __str__(self):
        return f"{self.package_name}{self.package_image}{self.no_of_day}{self.package_description}{self.package_price}"

    
    def admin_image(self):
        return mark_safe('<img src="{}" width="150"/>'.format(self.package_image.url))


