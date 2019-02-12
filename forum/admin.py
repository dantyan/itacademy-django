from django.contrib import admin

from forum.models import Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    pass
