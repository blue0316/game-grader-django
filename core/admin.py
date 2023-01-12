from django.contrib import admin
from core.models import User, InviteTeam, TeamDetail

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('uuid','username','email','password','role')

@admin.register(TeamDetail)
class InviteTeamAdmin(admin.ModelAdmin):
    list_display = ('user','team_name','team_code')

@admin.register(InviteTeam)
class TeamDetailAdmin(admin.ModelAdmin):
    list_display = ('invite_by','invite_to','team')