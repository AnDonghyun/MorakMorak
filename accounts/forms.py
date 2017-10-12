from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import Profile

class SignupForm(UserCreationForm):
    phone_number = forms.CharField()
    address = forms.CharField()

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self):
        user = super().save()
        Profile.object.create(
            user = user, 
            phone_number = self.cleaned_data['phone_number'],
            address = self.cleaned_data['address'],
            )
        return user


        
        
class LoginForm(AuthenticationForm):
    answer = forms.IntegerField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', None)
        if answer != 6:
            raise forms.ValidationError('Mismatched!')
        return answer
 #로그인 form을 만들어서 로그인 할 때 추가적인 인증 절차를 만들 수 있다. (이진석 34강)