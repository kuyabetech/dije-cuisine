from django import forms 
from django.forms import ModelForm
from .models import *

class ProfileCreation(ModelForm):
    class Meta:
        models = Profile
        fields = "__all__"
        

class CompanyCreation(ModelForm):
    class Meta:
        models = Company
        fields = '__all__'
        

class Products(ModelForm):
    class Meta:
        models = Product
        fields = "__all__"