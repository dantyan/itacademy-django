from datetime import datetime

from django.contrib import admin

from forum.models import Comment, Post, Tag, Thread


@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    search_fields = ['title']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ['tags']
    autocomplete_fields = ['thread']

    class Media:
        js = ("ckeditor/ckeditor.js", 'js/admin.js',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'post', 'user', 'add_time']
    list_filter = ['post', 'user', 'add_time']
    date_hierarchy = 'add_time'
    list_editable = ['user']
    actions = ['make_published']

    def make_published(self, request, queryset):
        queryset.update(add_time=datetime.now())

    make_published.short_description = 'Make add time today'



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
