from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.db import models


# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, is_active=True, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(default='', max_length=10, unique=True)
    email = models.EmailField(unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # first_name = models.CharField(default='', max_length=60, blank=True)
    # last_name = models.CharField(default='', max_length=60, blank=True)
    # current_position = models.CharField(default='', max_length=64, blank=True)
    #about = models.CharField(default='', max_length=255, blank=True)
    #grade = models.IntegerField(default='', blank=True)
    #faculty = models.CharField(default='', max_length=128, blank=True)
    #department = models.CharField(default='', max_length=128, blank=True)
    #company = models.CharField(default='', max_length=128, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    icon_id = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["email"]
    objects = MyUserManager()

    def __str__(self):
        return self.email