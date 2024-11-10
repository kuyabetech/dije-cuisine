from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StaffRegistrationFrom(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        def save(self, commit=False):
            user = super().save(commit=True)
            user.is_staff = True
            if commit:
                user.save()
                return user