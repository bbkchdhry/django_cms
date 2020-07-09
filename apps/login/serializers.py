from .user_authenticate import authenticate
from rest_framework import serializers, exceptions


class LogInSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        print("attrs are: ")
        print(attrs)
        email = attrs.get("email", "")
        password = attrs.get("password", "")

        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                print(user)
                if user.is_active:
                    attrs["user"] = user
                else:
                    msg = "User is not active anymore!"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Username and password doesnot match!"
                raise exceptions.ValidationError(msg)
        else:
            msg = "Enter username and password"
            raise exceptions.ValidationError(msg)
        return attrs
