from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager
import uuid
from django.utils.translation import gettext as _



# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The UserName field must be set')
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
    uuid = models.CharField(max_length=50, primary_key=True)
    # uuid = models.UUIDField(auto_created=True ,max_length=8, primary_key=True, default=uuid.uuid4)
    # uuid = models.UUIDField(primary_key=True, max_length=8, default=uuid.uuid4)
    username = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=12, null=True, blank=True)
    role = models.CharField(max_length=10, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    graduation = models.IntegerField(null=True, blank=True)
    seasonofaccess = models.CharField(max_length=500,null=True, blank=True)
    biography = models.CharField(max_length=500, null=True, blank=True)
    positions = models.CharField(max_length=500, null=True, blank=True)
    tags = models.CharField(max_length=500, null=True, blank=True)
    coverpic = models.ImageField(upload_to='cover_pic', null=True, blank=True)
    transcript = models.FileField(upload_to='transcript_pic', null=True, blank=True)
    document = models.FileField(upload_to='document_pic', null=True, blank=True)
    # profile_pic = models.ImageField(upload_to='profile', null=True, blank=True)
    # code = models.CharField(max_length = 50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
 
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    # def __str__(self):
    #     return "%s %s"%(self.first_name,self.last_name)
    def __str__(self):
        return "%s"%(self.username)

class TeamDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    team_name = models.CharField(max_length=50)
    team_code = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s"%(self.team_name)


class InviteTeam(models.Model):
    invite_by = models.ForeignKey(User,on_delete=models.CASCADE, related_name='invite_by')
    invite_to = models.ForeignKey(User,on_delete=models.CASCADE, related_name='invite_to')
    team = models.ForeignKey(TeamDetail,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class ActiveTeam(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    active_team = models.ForeignKey(TeamDetail,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class TeamMember(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user')
    teamname = models.ForeignKey(TeamDetail,on_delete=models.CASCADE)
    member = models.ForeignKey(User,on_delete=models.CASCADE, related_name='team_member')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "%s"%(self.member)

class NewGame(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    event = models.CharField(max_length=100)
    eventdate = models.DateField(null=True, blank=True)
    sharewith = models.ManyToManyField(User, related_name='sharewith')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
