from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models



class UserManager(UserManager):
    pass

class Nationality(models.Model):
    country = models.CharField(max_length=64)
    nationality = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    is_valid = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)


class User(AbstractUser):
    MALE = 1
    FEMALE = 2
    GENDER_CHOICES = (
        (MALE, 'male'),
        (FEMALE, 'female')
    )
    phone_number = models.CharField(unique=True, max_length=12)
    nationality = models.ForeignKey(Nationality, related_name='users_nationality', null=True, on_delete=models.SET_NULL)
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    is_valid = models.BooleanField(default=True)
    date_of_join = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

