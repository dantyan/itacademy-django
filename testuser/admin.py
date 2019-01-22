from django.contrib import admin

from testuser.models import TestUser


@admin.register(TestUser)
class TestUserAdmin(admin.ModelAdmin):
    pass
