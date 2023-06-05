from django.db import models

# Create your models here.

class Register(models.Model):
    username = models.CharField(max_length=100)
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    confirmpassword=models.CharField(max_length=100)

    def _str_(self):                
        return f"{self.username}{self.firstname}{self.lastname}{self.phone}{self.email}{self.password}{self.confirmpassword}"
    
