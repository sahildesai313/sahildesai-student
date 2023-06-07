from django.db import models


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


class package_details(models.Model):
    package_name =models.CharField(max_length=20)
    no_of_day =models.IntegerField()
    package_description =models.TextField()
    package_price=models.IntegerField()
   
    def __str__(self):
        return f"{self.package_name}{self.no_of_day}{self.package_description}{self.package_price}"
