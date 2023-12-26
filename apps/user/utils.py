import random
from django.utils.crypto import get_random_string


def session_token():
    token = get_random_string(length=32)
    return token


def generate_code():
    code = str(random.randint(10000, 99999))
    return code
