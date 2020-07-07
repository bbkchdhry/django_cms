from django import forms
from .models import User

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