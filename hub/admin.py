# hub/admin.py
from django.contrib import admin
from .models import MyNovel

# Register your models here.

@admin.register(MyNovel)
class HubAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'is_shared', 'created_at']
    list_display_links = ['title']
    list_editable = ['is_shared']
