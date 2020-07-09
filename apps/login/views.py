from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from django.contrib import messages

from .serializers import LogInSerializer

# Create your views here.
from rest_framework.views import APIView


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

logged_in_state = False

class login_validate(APIView):
    def post(self, request):
        global logged_in_state
        data = request.data
        serializer = LogInSerializer(data=data)
        if serializer.is_valid():
            logged_in_state = True
            context = {
                'title': 'Dashboard'
            }
            return render(request, 'index.html', context)
        elif serializer.errors:
            logged_in_state = False
            print(serializer.errors)
            messages.error(request, serializer.errors["non_field_errors"][0])
            return redirect('login_view')

    def get(self, request):
        global logged_in_state
        if logged_in_state == True:
            context = {
                'title': 'Dashboard'
            }
            return render(request, 'index.html', context)
        else:
            return redirect('login_view')