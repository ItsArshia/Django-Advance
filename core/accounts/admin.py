from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['email', 'is_superuser','is_active', 'create_at']
    list_filter = ['email', 'is_superuser', 'is_active']
    search_fields = ['email']
    ordering = ('create_at',)
    fieldsets = [
        ('Identify', {
            'fields': ('email', 'password')
        }),
        ('Permissions', {
            'fields': ('is_superuser','is_staff', 'is_active')
        }),
        ('Group_Permissions', {
            'fields': ('groups', 'user_permissions')
        }),
        ('Dates', {
            'fields': ('last_login',)
        })
    ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

admin.site.register(Profile)