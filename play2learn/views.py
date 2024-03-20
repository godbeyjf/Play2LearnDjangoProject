from django.shortcuts import render

def my_account_view(request):
    # Add any additional context data you need
    context = {}
    return render(request, 'account/myaccount.html', context)

def home_view(request):
    # Add any additional context data you need
    context = {}
    return render(request, 'home.html', context)