from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            backend = 'django.contrib.auth.backends.ModelBackend'
            user.backend = backend
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = CustomUserAuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def my_account_view(request):
    return render(request, 'account/myaccount.html')
