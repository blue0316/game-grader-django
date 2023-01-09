from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # ROLE_CHOISE = (
    #     ('admin','ADMIN'),
    #     ('Staff','STAFF'),
    #     ('ATHLATE','ATHLETE'),
    # )
    profile_pic = models.ImageField(upload_to='uploads', null=True, blank=True)
    code = models.CharField(max_length = 50, null=True, blank=True)
    # code = models.CharField(max_length = 20, choices = ROLE_CHOISE)

