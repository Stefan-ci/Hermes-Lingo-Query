from accounts.models import User
from django.contrib import admin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _


class UserAdmin(admin.ModelAdmin):
    list_display = ["api_key", "email", "username", "is_active", "is_superuser", "date_joined"]
    search_fields = ["email", "username", "is_active", "is_staff", "is_admin", "is_superuser", "date_joined",
        "first_name", "last_name", "last_login", "api_key"]
    list_filter = ["is_active", "is_staff", "is_admin", "is_superuser", "date_joined"]
    date_hierarchy = "date_joined"
    
    
    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_add_permission(self, request, obj=None):
        return False
    
    def has_changes_permission(self, request, obj=None):
        return False

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
