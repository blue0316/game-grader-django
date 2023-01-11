from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
import uuid
from django.utils.translation import gettext as _



# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The UserName field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
 
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username, password, **extra_fields)

class User(AbstractUser):
    uuid = models.CharField(max_length=50, primary_key=True, default=uuid.uuid4)
    username = models.CharField(max_length=1000, unique=True, blank=True, null = True)
    profile_pic = models.ImageField(upload_to='uploads', null=True, blank=True)
    # code = models.CharField(max_length = 50, null=True, blank=True)
    role = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class InviteTeam(models.Model):
    invite_by = models.ForeignKey(User,on_delete=models.CASCADE)
    invite_to = models.CharField(max_length = 50)
    code = models.CharField(max_length = 50, null=True, blank=True)
    role = models.CharField(max_length = 50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
