from django.conf import settings 
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


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
