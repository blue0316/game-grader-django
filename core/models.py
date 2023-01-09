from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not username:
            raise ValueError('The UserName field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    # ROLE_CHOISE = (
    #     ('admin','ADMIN'),
    #     ('Staff','STAFF'),
    #     ('ATHLATE','ATHLETE'),
    # )
    profile_pic = models.ImageField(upload_to='uploads', null=True, blank=True)
    # code = models.CharField(max_length = 50, null=True, blank=True)
    # code = models.CharField(max_length = 20, choices = ROLE_CHOISE)
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
