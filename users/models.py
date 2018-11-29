from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.db import models


def validate_email(email):
    """validation that the email is valid"""
    try:
        def check_email(email):
            """
            Function that verifies that the string passed is a valid email address.

            :param email: The potential email address
            :type email: :py:class:`str`
            :return: Nothing
            """
            if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
                raise ValueError('String passed is not a valid email address')
            return
    except ValueError:
        raise ValidationError("Email address is not valid.")


class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email
