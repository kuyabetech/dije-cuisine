from django.db import models
# from django.contrib.auth.models import User

class Profile(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    phone = models.IntegerField()
    pic = models.FileField(upload_to="profile")
    
    def __str__(self):
        return self.first_name
    
    
class Company(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.FileField(upload_to="comp/images")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    price = models.IntegerField()
    
    
    def __str__(self):
        return self.name