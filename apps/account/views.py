import json

from django.forms import model_to_dict
from django.shortcuts import render, redirect
from rest_framework.response import Response
from .delete_authenticate import deleteAuthenticate
from rest_framework import status
from rest_framework.views import APIView
from .forms import UserForm, UserRolesForm
from .models import User, User_role
from .serializers import UserSerializers, UserRolesSerializers
from .hashing import get_salt, hash_string
from ..login.decorators import my_login_required
from apps.roles.models import Role


# Create your views here.

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

class dashboard_page_7(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard-7'
        }
        return render(request, 'dashboard_7.html', context)

class panel_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Panel'
        }
        return render(request, 'basic_ui/panels.html', context)

class tabs_line_pill_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Tabs'
        }
        return render(request, 'basic_ui/tabs-pill-line.html', context)

class alert_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Alert'
        }
        return render(request, 'basic_ui/alerts.html', context)

class tooltip_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': "Dashboard - Tooltip"
        }
        return  render(request, 'basic_ui/tooltip_popover.html', context)

class badges_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': "Dashboard - Badges Progress"
        }
        return render(request, 'basic_ui/badges_progress.html', context)

class list_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - List'
        }
        return render(request, 'basic_ui/lists.html', context)

class toastr_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Toastr'
        }
        return render(request, 'components/toastr.html', context)


class sweet_alert_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - SweetAlert'
        }
        return render(request, 'components/sweetalert.html', context)

class alertify(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Alertify'
        }
        return render(request, 'components/alertify.html', context)

class idle_timer_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Idle-Timer'
        }
        return render(request, 'components/idle_timer.html', context)

class session_timeout_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Session-Timeout'
        }
        return render(request, 'components/session_timeout.html', context)

class tree_view_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Tree View'
        }
        return render(request, 'components/tree_view.html', context)

class nestable_list_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Nestable List'
        }
        return render(request, 'components/nestable.html', context)

class clipboard_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Clipboard'
        }
        return render(request, 'components/clipboard.html', context)

class button_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Buttons'
        }
        return render(request, 'buttons/buttons.html', context)

class widget_list_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Widget List'
        }
        return render(request, 'widgets/widgets-list.html', context)

class form_control_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Form Control'
        }
        return render(request, 'forms/form-controls.html', context)

class form_switch_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Form Switch'
        }
        return render(request, 'forms/form-switch.html', context)

class form_layout_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Form Layout'
        }
        return render(request, 'forms/form_layouts.html', context)

class form_input_group_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Form Input Group'
        }
        return render(request, 'forms/form-input-groups.html', context)

class form_checkbox_radio_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Form Checkbox-Radio'
        }
        return render(request, 'forms/form-checkbox-radio.html', context)

class form_advanced_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Form Advanced'
        }
        return render(request, 'forms/form_advanced.html', context)

class form_mask_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Form Mask'
        }
        return render(request, 'forms/form_masks.html', context)

class form_validation_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Form Validation'
        }
        return render(request, 'forms/form_validation.html', context)

class text_editor_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Text Editor'
        }
        return render(request, 'forms/text_editors.html', context)

class form_dropzone_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Form Dropzone'
        }
        return render(request, 'forms/form_dropzone.html', context)

class image_cropping_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Image Cropping'
        }
        return render(request, 'forms/image_cropping.html', context)

class autocomplete_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Auto Complete'
        }
        return render(request, 'forms/autocomplete.html', context)

class datatables_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Datatables'
        }
        return render(request, 'forms/datatables.html', context)

class form_wizard_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Form Wizard'
        }
        return render(request, 'forms/form_wizard.html', context)

class chart_js_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - ChartJs'
        }
        return render(request, 'chartjs/chartjs.html', context)

class google_map_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Google Map'
        }
        return render(request, 'maps/maps_google.html', context)

class calendar_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Calendar'
        }
        return render(request, 'pages/calendar.html', context)

class faq_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - FAQ'
        }
        return render(request, 'pages/faq.html', context)

class login_v2_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - LogIn v2'
        }
        return render(request, 'pages/custom_pages/user_page/login-2.html', context)

class login_v3_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - LogIn v3'
        }
        return render(request, 'pages/custom_pages/user_page/login-4.html', context)

class login_v4_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - LogIn v4'
        }
        return render(request, 'pages/custom_pages/user_page/login-5.html', context)

class forgot_password_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Forgot Password'
        }
        return render(request, 'pages/custom_pages/user_page/forgot_password.html', context)

class error_404_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Error 404'
        }
        return render(request, 'pages/custom_pages/error_page/error_404.html', context)

class error_403_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Error 403'
        }
        return render(request, 'pages/custom_pages/error_page/error_403.html', context)

class error_500_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Error 500'
        }
        return render(request, 'pages/custom_pages/error_page/error_500.html', context)

class maintenance_page(APIView):
    @my_login_required
    def get(self, request):
        context = {
            'title': 'Dashboard - Maintenance'
        }
        return render(request, 'pages/custom_pages/error_page/maintenance.html', context)

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

class deleteConfirmation(APIView):
    def post(self, request, password):
        user = deleteAuthenticate(request, password)
        if user:
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)



# def deleteConfirmation(request, password):
#     user = request.session['username']
#     user_model = User.objects.get(user_name = user)
#     salt = user_model.salt
#
#     print(user)
#     print(user_model)
#     print("password is: ")
#     print(password)


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
