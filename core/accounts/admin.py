from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
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