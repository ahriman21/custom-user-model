from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib.auth.models import Group
from . import admin_forms
# Register your models here.


class UserAdmin(UserAdmin):
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
