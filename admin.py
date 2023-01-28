from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from . import forms
from django.contrib.auth.models import Group

# Register your models here.


class UserAdmin(BaseUserAdmin):
    

    list_display = ('email','phone','_role')
    list_filter = ('is_superuser','_role')
    search_fields = ('email',)
    readonly_fields = ('last_login','join_date')

    fieldsets = (
        (None, {'fields': ('email', 'password','full_name','phone','city','address')}),
        ('Permissions',
         {'fields': ('_role',
                    'last_login',
                     'join_date',
                     'groups',
                    'user_permissions')
         }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','full_name','city','phone','address', 'password1', 'password2'),
        }),
    )
    ordering = ('full_name','id')
    filter_horizontal = ('groups','user_permissions')
##
admin.site.register(User,UserAdmin)
