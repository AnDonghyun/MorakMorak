
from django.contrib import admin
from .models import StartRelayNovel, RelayNovelSequel, RadioStation, MomoReply
# Register your models here.

@admin.register(StartRelayNovel)
class StartRelayNovelAdmin(admin.ModelAdmin):
    list_display =['id','author','title', 'content', 'created_at', 'updated_at']
    

@admin.register(RelayNovelSequel)
class RelayNovelSequelAdmin(admin.ModelAdmin):
    list_display = ['StartRelayNovel', 'author', 'summary', 'content','created_at', 'updated_at']


@admin.register(RadioStation)
class RelayNovelSequelAdmin(admin.ModelAdmin):
    list_display = ['writer', 'content','created_at', 'updated_at']


@admin.register(MomoReply)
class RelayNovelSequelAdmin(admin.ModelAdmin):
    list_display = ['RadioStation', 'content','created_at', 'updated_at']

    