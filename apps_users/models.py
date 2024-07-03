from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.hashers import make_password
import uuid

from helper.utils import *

class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields) 

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)
    last_name = models.CharField(max_length=MAX_STR_LEN, null=True, blank=True)
    user_type = models.CharField(max_length=MAX_STR_LEN, choices=[(utype, utype) for utype in USER_TYPES], null=True, blank=True)

    programme = models.CharField(max_length=MAX_STR_LEN, choices=[(utype, utype) for utype in PROGRAMME], null=True, blank=True)
    year = models.CharField(max_length=MAX_STR_LEN, choices=[(year, year) for year in YEAR_TYPE], null=True, blank=True)
    college = models.CharField(max_length=MAX_STR_LEN, choices=[(college, college) for college in COLLEGE], null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} - {self.user_type}"
    