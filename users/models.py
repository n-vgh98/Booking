from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import RegexValidator
from django.utils import timezone
from django.db import models


class Nationality(models.Model):
    country = models.CharField(max_length=64)
    nationality = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class CustomUserManager(BaseUserManager):

    def create_user(self, phone_number, password, **extra_fields):
        if not phone_number:
            raise ValueError(_('The Email must be set'))
        # phone_number = self.phone_number
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(unique=True, validators=[phone_regex], max_length=17,)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __Str__(self):
        return self.phone_number

    # @property
    # def token(self):
    #     return self._generate_jwt_token()


class Profile(models.Model):
    first_name = models.CharField(max_length=150, blank=True, verbose_name="first name")
    last_name = models.CharField(max_length=150, blank=True, verbose_name="last name")
    email = models.EmailField(max_length=254, blank=True, verbose_name="email address", unique=True)
    user_name = models.CharField(max_length=64, blank=True, verbose_name="user name")
    user = models.ForeignKey(User, related_name='user_profile', on_delete=models.CASCADE)
    nationality = models.ForeignKey(Nationality, related_name='user_nationality', null=True, blank=True, on_delete=models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

