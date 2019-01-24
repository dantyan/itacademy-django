from django.contrib import admin

from testuser.models import TestUser


@admin.register(TestUser)
class TestUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'join_date', 'is_active', 'birth_date']
    list_filter = ['is_active', 'birth_date']
    date_hierarchy = 'birth_date'
