# practice/models.py
from django.db import models
from django.contrib.auth.models import User


class StartRelayNovel(models.Model):
    author = models.OneToOneField(User)
    title = models.CharField(max_length=100, verbose_name='소설 제목') #릴레이 소설 제목
    content = models.TextField(help_text='새로운 릴레이 소설의 문을 열어보세요!') #첫번째로 작성된 소설
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RelayNovelSequel(models.Model):
    author = models.OneToOneField(User)
    StartRelayNovel = models.ForeignKey(StartRelayNovel)
    summary = models.TextField(help_text='이어지는 내용을 짧게 요약해 주세요!')
    content = models.TextField(help_text='재치있게 소설을 이어나가 보세요!')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class RadioStation(models.Model):
    writer = models.CharField(max_length=20, verbose_name='보내는 이')
    content = models.TextField(help_text='모모언니에게 사연을 보내보세요!')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MomoReply(models.Model):
    RadioStation = models.ForeignKey(RadioStation)
    content = models.TextField(help_text='모모언니가 되어 사연에 답장해보세요!')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

