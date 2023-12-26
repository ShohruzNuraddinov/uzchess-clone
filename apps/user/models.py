from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from phonenumber_field.modelfields import PhoneNumberField
from apps.user.managers import UserManager
from apps.utils.models import BaseModel
from random import randint
# Create your models here.

PHONE_NUMBER = 'phone_number'
EMAIL = 'email'

auth_type_choices = (
    ('phone_number', PHONE_NUMBER),
    ('email', EMAIL),
)


class User(AbstractBaseUser, PermissionsMixin):
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    full_name = models.CharField(
        _('Full Name'), max_length=256, blank=True, null=True)

    birthed_at = models.DateField(blank=True, null=True)

    phone_number = PhoneNumberField(
        _('Phone Number'), unique=True, null=True, blank=True)
    email = models.EmailField(_('Email'), unique=True, blank=True, null=True)

    pic = models.ImageField(upload_to='user/pic/', blank=True, null=True)

    auth_type = models.CharField(
        max_length=128, choices=auth_type_choices, blank=True, null=True)

    objects = UserManager()

    def __str__(self):
        if self.phone_number:
            return str(self.phone_number)
        else:
            return self.email

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name', 'email']

    @staticmethod
    def has_perm(perm, obj=None, **kwargs):
        return True

    @staticmethod
    def has_module_perms(app_label, **kwargs):
        return True


class OTPModel(BaseModel):
    phone_number_or_email = models.CharField(max_length=512)
    code = models.IntegerField()
    active_till = models.DateTimeField(blank=True, null=True)
    lifetime = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.phone_number)

    def get_random_code(self):
        code = randint(100000, 999999)
        return code
