from rest_framework import serializers
from .models import User, User_role


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "salt": {'read_only': True},
            "hashed_password": {'read_only': True}
        }

class UserRolesSerializers(serializers.ModelSerializer):

    class Meta:
        model = User_role
        fields = "__all__"