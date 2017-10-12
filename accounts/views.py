from django.conf import settings 
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm, LoginForm

from django.contrib.auth.views import login as auth_login
from allauth.socialaccount.models import SocialApp
from allauth.socialaccount.templatetags.socialaccount import get_providers


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(settings.LOGIN_URL) #default : "/accounts/login/"
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html',{
        'form': form,
        
        })

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


def login(request):
    providers = []
    for provider in get_providers(): #settings/INSTALLED_APPS 내에서 활성화 된 목록
    # social_app속성은 provider에는 없는 속성입니다.
        try:
            #실제 PROVIDER 별 CLINET ID/PW가 등록되어 있는가?
            provider.social_app = SocialApp.objects.get(provider=provider.id, sites=settings.SITE_ID)
        except SocialApp.DoesNotExist:
            provider.social_app = None
        providers.append(provider)
    
    return auth_login(request,
        authentication_form=LoginForm,
        template_name='accounts/login_form.html',
        extra_context={'providers': providers})
    
