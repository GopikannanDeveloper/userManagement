from django.contrib.auth.models import AbstractUser, Group, Permission
from django.contrib.auth.models import UserManager
from django.db import models
import uuid

class CustomUserManager(UserManager):
    def _create_user(self, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault('is_active', True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    userid = models.UUIDField(primary_key=True, editable=False)
    email = models.EmailField(unique=True)
    verified_user = models.BooleanField(default=False)
    user_active = models.BooleanField(default=False)
    
    objects = CustomUserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = "email"
    
