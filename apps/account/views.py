from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .forms import UserForm
from .models import User
from .serializers import UserSerializers
from .hashing import get_salt, hash_string
from rest_framework import HTTP_HEADER_ENCODING

# Create your views here.
from ..login.decorators import my_login_required


class user_page(APIView):
    @my_login_required
    def get(self, request):
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'user/users.html', context)


class user_view(APIView):
    print("getting......")
    def get(self, request):
        users = User.objects.all()
        user_serializer = UserSerializers(users, many=True)
        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        print("posting......")
        data = request.data
        print("data is......")
        print(data)
        salt = get_salt()
        hashed_password = hash_string(salt, data["password"])
        serializer = UserSerializers(data=data)
        if serializer.is_valid():
            serializer.save(salt=salt, hashed_password=hashed_password)
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif serializer.errors:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class user_view_detail(APIView):
    def get_object(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist as e:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        instance = self.get_object(id)
        print(model_to_dict(instance))
        serializer = UserSerializers(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, id):
        instance = self.get_object(id)
        data = request.data
        print("instance is: ")
        print(model_to_dict(instance))
        print("data is: ")
        print(data)
        serializer = UserSerializers(data=data, instance=instance, partial=True)
        if serializer.is_valid():
            print("Valid......")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif serializer.errors:
            print("Errors.....")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        instance = self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)