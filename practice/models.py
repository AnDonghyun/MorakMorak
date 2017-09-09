# practice/models.py
from django.db import models

class Post(models.Model):
    header = models.OneToOneField('Type')
    title = models.CharField(max_length=100)
    series = models.CharField(max_length=10, blank=True, default='0')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Type(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
