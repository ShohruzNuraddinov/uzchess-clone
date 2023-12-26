from django.shortcuts import render
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.user.models import User, PHONE_NUMBER, EMAIL
from apps.user.serializers import UserSendCodeSerializer, UserCodeVerifySerializer, UserSetPasswordSerializer
from apps.user.utils import generate_code, session_token
# Create your views here.


class UserSendVerificationCodeView(generics.GenericAPIView):
    serializer_class = UserSendCodeSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        session = session_token()
        code = generate_code()

        print(code)

        full_name = data.get('full_name', None)

        auth_data = {
            'session': session,
            'code': code
        }

        if data.get('auth_type', None) == PHONE_NUMBER:
            phone_number = data.get('phone_number', None)
            if cache.get(phone_number, None) is not None:
                return Response(
                    {
                        'message': _('This Phone Number already sent code!')
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            user_data = {
                'full_name': full_name,
                'phone_number': phone_number,
            }

            cache.set(phone_number, auth_data, 120)
            data.update({'session': session})
        else:
            email = data.get('email', None)
            if cache.get(email, None) is not None:
                return Response(
                    {
                        'message': _('This Email already sent code!')
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            user_data = {
                'full_name': full_name,
                'email': email,
            }

            cache.set(email, auth_data, 120)
            data.update({'session': session})

        cache.set(session, user_data, 300)
        return Response(data)


class UserCodeVerifyView(generics.GenericAPIView):
    serializer_class = UserCodeVerifySerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        phone_number_or_email = data.get('phone_number_or_email', None)
        session = data.get('session', None)
        code = data.get("code", None)

        auth_cache_data = cache.get(phone_number_or_email, None)

        if auth_cache_data is None:
            return Response(
                {
                    'message': _('This Phone number or Email sent code already expired.')
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if auth_cache_data['code'] != code:
            return Response(
                {
                    'message': _("Incorrect code.")
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        auth_data = cache.get(session)
        auth_data.update({'is_active': True})
        cache.set(session, auth_data)

        data = {
            'message': _('Successfully verification'),
            'session': session
        }

        return Response(data, status=status.HTTP_200_OK)


class UserSetPasswordView(generics.GenericAPIView):
    serializer_class = UserSetPasswordSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        session = data.get('session', None)
        password = data.get('password', None)

        cache_data = cache.get(session, None)

        if cache_data is None:
            return Response(
                {
                    'message': _("Invalid session.")
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        is_active = cache_data.pop('is_active')

        if not is_active:
            return Response(
                {
                    'message': _("Not Active!")
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User(**cache_data)
        user.set_password(password)
        user.save()
        data = {
            'message': _("Successfully create user."),
        }
        return Response(data, status=status.HTTP_201_CREATED)


