"""
User admin panel
"""
from django.contrib import admin
from .models import User
from .forms import UserChangeForm,UserCreationForm

class UserAdmin(admin.ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'full_name', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('full_name','email','city')
    readonly_fields = ('last_login','join_date')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name','city')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'full_name', 'password1', 'password2'),
        }),
    )

    ordering = ('email',)
    filter_horizontal = ('groups','user_permissions')


admin.site.register(User,UserAdmin)
