from django import forms
from .models import User, User_role
from apps.roles.models import Role

class UserForm(forms.ModelForm):
    is_superuser = forms.BooleanField(initial=False,
                                      widget=forms.RadioSelect(choices=[(True, 'Yes'),
                                                            (False, 'No')],
                                         ))

    is_active = forms.BooleanField(initial=False,
                                      widget=forms.RadioSelect(choices=[(True, 'Yes'),
                                                                        (False, 'No')],
                                                               ))
    class Meta:
        model = User
        fields = "__all__"


class UserRolesForm(forms.ModelForm):
    roles = forms.ModelMultipleChoiceField(
        queryset=Role.objects,
        widget=forms.SelectMultiple,
        required=True)
    class Meta:
        model = User_role
        fields = "__all__"