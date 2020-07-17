import json

from django.forms import model_to_dict
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .forms import UserForm, UserRolesForm
from .models import User, User_role
from .serializers import UserSerializers, UserRolesSerializers
from .hashing import get_salt, hash_string
from rest_framework import HTTP_HEADER_ENCODING
import ast
# Create your views here.
from ..login.decorators import my_login_required
from apps.roles.models import Role
from django.contrib import messages

class user_page(APIView):
    """View to render user.html page"""
    @my_login_required
    def get(self, request):
        form = UserForm()
        context = {
            'form': form,
            'title': "Dashboard - User"
        }
        return render(request, 'user/users.html', context)


class user_view(APIView):
    """APIView of the user..."""
    def get(self, request):
        """Get request to list all the users..."""
        print("getting user view")
        users = User.objects.all()
        user_serializer = UserSerializers(users, many=True)
        return Response({"data": user_serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        """Post request to create new users..."""
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
    """User APIView to retrieve specific user"""
    def get_object(self, id):
        """Returns user of specific id...."""
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist as e:
            return Response({'error': 'User does not exist'}, status=status.HTTP_404_NOT_FOUND)


    def get(self, request, id):
        """Get request to retrieve user of specific user id..."""
        print("getting specific.....")
        instance = self.get_object(id)
        print(model_to_dict(instance))
        serializer = UserSerializers(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id):
        """Put request to update the user of specific id...."""
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
        """Delete request to remove the user of specific id..."""
        print("deleting....")
        instance = self.get_object(id)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class user_role_page(APIView):
    @my_login_required
    def get(self, request):
        form = UserRolesForm()
        context = {
            "form": form,
            "title": "Dashboard - UserRoles"
        }
        return render(request, 'user_role/user_roles.html', context)

class user_roles_view(APIView):
    def get(self, request):
        user_role = User_role.objects.all()
        serializer = UserRolesSerializers(user_role, many=True)
        list_data = []
        for data in serializer.data:
            user_model = User.objects.get(id=data["user"])
            role = []
            for role_id in data["roles"]:
                role_model = Role.objects.get(id=role_id)
                role.append(role_model.name)
            data = {
                "id": data["id"],
                "user": user_model.user_name,
                "roles": role
            }
            list_data.append(data)

        return Response({"data": list_data}, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = UserRolesSerializers(data={'user': data["user"], 'roles': request.data.getlist("roles[]")})
        if serializer.is_valid():
            serializer.save()
            user = serializer.validated_data["user"]
            roles = [role_name.name for role_name in serializer.validated_data["roles"]]
            print(user.user_name)
            print(roles)
            data = {
                "id": serializer.data["id"],
                "user": user.user_name,
                "roles": roles
            }
            return Response(data, status=status.HTTP_201_CREATED)
        elif serializer.errors:
            print("Errors...")
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class user_roles_view_detail(APIView):
    def get_object(self, id):
        try:
            return User_role.objects.get(id=id)
        except User_role.DoesNotExist as e:
            return Response({'error': 'User roles does exists...'})

    def get(self, request, id):
        instance = self.get_object(id)
        serializer = UserRolesSerializers(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        instance = self.get_object(id)
        data = request.data
        print(model_to_dict(instance))
        print(data)
        serializer = UserRolesSerializers(data={'user': data['user'], 'roles': data.getlist('roles[]')}, instance=instance, partial=True)
        if serializer.is_valid():
            print("Valid....")
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif serializer.errors:
            print("Errors...")
            print(serializer.errors)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id):
        print("deleting....")
        instance = self.get_object(id)
        print(instance)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
