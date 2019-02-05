from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    pass
