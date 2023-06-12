from django.db import models
from django.contrib.auth.models import User
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



class resturants_details(models.Model):
    item_name = models.CharField(max_length=20)
    item_description = models.TextField(max_length=500 )
    items_price = models.IntegerField()
    photo = models.ImageField(upload_to='pics')


def __str__(self):
        return f"{self.item_name}{self.item_description}{self.items_price}{self.photo}"


class Grocery_details(models.Model):
    Grocery_name=models.CharField(max_length=200)
    Grocery_price=models.IntegerField()
    Grocery_description=models.TextField()
    photo=models.ImageField(upload_to='photo')


    def _str_(self):
      return f"{self.Grocery_name}{self.Grocery_price}{self.Grocery_description}"


class Medicin_details(models.Model):
    Medicin_name =models.CharField(max_length=100)
    Medicin_image=models.ImageField(upload_to="images")
    Do_description =models.TextField(default="")
    Medicin_price=models.IntegerField(default="")

    def __str__(self):
        return f"{self.Medicin_name}{self.Medicin_image}{self.Do_description}{self.Medicin_price}"

    def admin_image(self):
        return mark_safe('<img src="{}" width="150"/>'.format(self.Medicin_image.url))
   
