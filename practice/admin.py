
from django.contrib import admin
from .models import Post, Type
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =['id','header','title', 'series', 'created_at', 'updated_at']
    

    @admin.register(Type)
    class TypeAdmin(admin.ModelAdmin):
        list_display = ['name', 'created_at']