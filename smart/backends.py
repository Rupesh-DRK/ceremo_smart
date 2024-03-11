from django.contrib.auth.backends import ModelBackend
from .models import *
from django.contrib.auth.hashers import make_password,check_password
class CustomBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user_profile=userData1.objects.get(email=email)
            if user_profile.password:
                return user_profile
        except userData1.DoesNotExist:
            pass
        return None