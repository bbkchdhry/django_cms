from django.contrib.auth.decorators import login_required
from django.forms import model_to_dict
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib import messages

from .decorators import my_login_required
from .serializers import LogInSerializer
# Create your views here.
from rest_framework.views import APIView
from django.contrib.auth import login as django_login


def login_view(request):
    if not request.session.has_key('username'):
        context = {
            'title': 'Login'
        }
        return render(request, 'login.html', context)
    else:
       return redirect('dashboard')

def profile(request):
    context = {
        'title': 'Profile'
    }
    return render(request, 'profile.html', context)


class login_validate(APIView):
    def post(self, request):
        global user
        data = request.data
        serializer = LogInSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            request.session['username']=user.user_name
            context = {
                'title': 'Dashboard',
                'user': user.user_name
            }
            return render(request, 'index.html', context)
        elif serializer.errors:
            print(serializer.errors)
            messages.error(request, serializer.errors["non_field_errors"][0])
            return redirect('login_view')

    @my_login_required
    def get(self, request):
        user = request.session.get('username')
        context = {
            'title': 'Dashboard',
            'user': user
        }
        return render(request, 'index.html', context)

class logout(APIView):
    def get(self, request):
        try:
            del request.session['username']
        except:
            pass
        return redirect('login_view')