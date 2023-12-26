from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number=None, email=None, full_name=None, password=None):

        # if (phone_number or email) is not None:
        #     raise ValueError("Phone Number or Email Required")
        if (phone_number or email) is None:
            raise ValueError("Phone Number or Email is Required!!!")
        if password is None:
            raise ValueError("Password is Required!!!")

        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            full_name=full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number=None, email=None, full_name=None, password=None):
        user = self.create_user(
            phone_number=phone_number,
            email=email,
            full_name=full_name,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(
            models.Q(phone_number__iexact=username) |
            models.Q(email__iexact=username)
        )
