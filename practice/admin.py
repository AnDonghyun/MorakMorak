
from django.contrib import admin
from .models import StartRelayNovel, RelayNovelSequel, RadioStation, MomoReply
# Register your models here.

@admin.register(StartRelayNovel)
class StartRelayNovelAdmin(admin.ModelAdmin):
    list_display =['title', 'content', 'created_at', 'updated_at']
    

@admin.register(RelayNovelSequel)
class RelayNovelSequelAdmin(admin.ModelAdmin):
    list_display = ['StartRelayNovel', 'summary', 'content','created_at', 'updated_at']


@admin.register(RadioStation)
class RadioStationAdmin(admin.ModelAdmin):
    list_display = ['writer', 'content','created_at', 'updated_at']


@admin.register(MomoReply)
class MomoReplyAdmin(admin.ModelAdmin):
    list_display = ['RadioStation', 'content','created_at', 'updated_at']

    