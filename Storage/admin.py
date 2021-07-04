from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from .forms import MyUserForm, MyUserChangeForm

from .models import myUser

class MyUserAdmin(UserAdmin):
    add_form = MyUserForm
    form = MyUserChangeForm
    model = myUser
    fieldsets = (
        (None, {
            "fields": (
                'profile_picture', 'mobile_number', 'myroles'
            ),
        }),
    )
    
    
    
    

admin.site.register(myUser, MyUserAdmin)

