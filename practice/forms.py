from django import forms
from .models import StartRelayNovel

class PostForm(forms.ModelForm):
    # dummy = forms.CharField(widget=NaverMapPointWidget(attrs={'width':"100%", 'height':200}))

    class Meta:
        model = StartRelayNovel
        fields = '__all__'
