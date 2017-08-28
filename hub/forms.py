from django import forms
from .models import MyNovel

class PostForm(forms.ModelForm):
    # dummy = forms.CharField(widget=NaverMapPointWidget(attrs={'width':"100%", 'height':200}))

    class Meta:
        model = MyNovel
        fields = '__all__'
