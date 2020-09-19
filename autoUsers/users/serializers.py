from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    It's user registration model serializer.
    """

    user_password = serializers.CharField(
        source="password", style={"input_type": "password"}, max_length=20, min_length=8
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "user_password")

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        user.set_password(user.password)
        user.save()
        Token.objects.create(user=user)
        return user


class AuthTokenSerializer(serializers.Serializer):
    """
    It's authentication serializer. it's valid method check if
    not valid user raise exception or if authenticate
    return user.
    """

    email = serializers.EmailField(label=("email"))
    password = serializers.CharField(
        label=("Password"), style={"input_type": "password"}
    )

    def validate(self, attrs):
        username = attrs.get("email")
        password = attrs.get("password")

        if username and password:
            user_obj = User.objects.filter(email=username)
            if user_obj:
                user = authenticate(username=user_obj[0].email, password=password)

                if user:
                    if not user.is_active:
                        msg = {"user": "User account is disabled."}
                        raise serializers.ValidationError(msg, code="authorization")
                else:
                    msg = {"logging": "Unable to log in with provided credentials."}
                    raise serializers.ValidationError(msg, code="authorization")
            else:
                msg = {
                    "username": "username address is not correct or user is not valid user type."
                }
                raise serializers.ValidationError(msg, code="authorization")
        else:
            if not username and not password:
                msg = {
                    "username": 'Must include "email"',
                    "password": 'Must include "password".',
                }

            if not username:
                msg = {
                    "username": 'Must include "username"',
                }

            if not password:
                msg = {"password": 'Must include "password".'}

            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class UserLogoutSerializer(serializers.Serializer):
    """
    It's user logout serializer. it's logout on token bases.
    """

    token = serializers.CharField(label=("Token"))

    def validate(self, attrs):
        token = attrs.get("token")

        if token:
            token = Token.objects.filter(key=token)
            if not token:
                msg = {"token": "Invalid token."}
                raise serializers.ValidationError(msg, code="authorization")
        else:
            msg = {"token": 'Must include "token".'}
            raise serializers.ValidationError(msg, code="authorization")

        attrs["token"] = token
        return attrs
