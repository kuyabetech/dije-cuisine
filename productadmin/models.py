from django.db import models

# Create your models here.
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