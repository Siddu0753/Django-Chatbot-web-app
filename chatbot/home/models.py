from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField()


    def __str__(self):
        return self.name
   
class Register(models.Model):
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=50)


    def __str__(self):
        return self.name

