from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from .choices import USER_TYPE


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email address",max_length=255,unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField( max_length=50)
    profile_picture = models.ImageField(upload_to="profile_pics/", blank=True, null=True)
    user_type = models.CharField(max_length=1, choices=USER_TYPE, default="2")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = "email"
    
    def __str__(self):
        return self.email


class Address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    line1 = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pin_code = models.IntegerField(validators=[MaxValueValidator(999999),MinValueValidator(100000)])

    def __str__(self):
        return self.line1

