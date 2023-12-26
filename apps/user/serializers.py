from rest_framework import serializers
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from django.contrib.auth import authenticate

from apps.user.models import User, PHONE_NUMBER, EMAIL


class UserSendCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'full_name',
            'phone_number',
            'email',
        ]

    def validate(self, data):
        phone_number = data.get("phone_number", None)
        email = data.get("email", None)

        if phone_number:
            if email:
                raise ValidationError(
                    {
                        "error": _("You can enter only one of phone number and email at a time!"),
                    }
                )
            data.update({"auth_type": PHONE_NUMBER})
            return data

        if email:
            data.update({"auth_type": EMAIL})
            return data

        raise ValidationError(
            {
                "error": _("You must enter phone number or email!"),
            }
        )


class UserCodeVerifySerializer(serializers.Serializer):
    phone_number_or_email = serializers.CharField()
    session = serializers.CharField()
    code = serializers.CharField()


class UserSetPasswordSerializer(serializers.Serializer):
    session = serializers.CharField()
    password = serializers.CharField()


class UserLoginSerializer(serializers.Serializer):
    phone_number_or_email = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def create(self, validated_data):
        
        phone_number_or_email = validated_data.get("phone_number_or_email", None)
        password = validated_data.get("password", None)
        auth = authenticate(Q(phone_number_or_email) | Q(email=phone_number_or_email), password=password)
        if auth is None:
            return 

        return 