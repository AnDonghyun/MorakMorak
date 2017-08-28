# hub/models.py
import re
from django import forms
from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models

# Create your models here.

class MyNovel(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()
    is_shared = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.CharField(max_length=100, blank=True)
    STATUS_CHOICES = (
        ('d', '작성중'),
        ('f', '작성완료'),
        ('p', '출판'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES) 


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('hub:mynovel', args=[self.pk])



