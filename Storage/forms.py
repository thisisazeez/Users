from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . models import myUser

class MyUserForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = myUser
        fields = ('username', 'profile_picture', 'mobile_number', 'myroles')
        
class MyUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm):
        model = myUser
        fields = ('username', 'profile_picture', 'mobile_number', 'myroles')