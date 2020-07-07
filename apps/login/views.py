from django.shortcuts import render

# Create your views here.
def login_view(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'login.html', context)

def login(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'index.html', context)

def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'profile.html', context)

