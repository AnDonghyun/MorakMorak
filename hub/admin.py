# hub/admin.py
from django.contrib import admin
from .models import MyNovel

# Register your models here.

@admin.register(MyNovel)
class HubAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'created_at', 'status']
    list_display_links = ['title']
    list_editable = ['status']
